import json
from pprint import pprint

import paho.mqtt.client as mqtt
try:
    import urlparse
    parse = urlparse.urlparse
except ModuleNotFoundError:
    from urllib.parse import urlparse as parse


class Broker:
    def __init__(self):
        url = "mqtt://iot.eclipse.org:1883/boomatang/home"
        self.url = parse(url)
        self.base_topic = self.url.path[1:]
        self.mqttc = mqtt.Client()
        self.setup_mqtt()
        self.payload = {}
        self.topic = None
        self.remote_action_flag = 'remote action'
        self.remote_actions = {}
        self.call = 0


    # Define event callbacks
    def on_connect(self, client, userdata, flags, rc):
        print("Connection Result; " + str(rc))

    def on_publish(self, client, obj, mid):
        print("Message ID: " + str(mid))

    def on_message(self, client, obj, msg):
        self.topic = msg.topic[len(self.base_topic)+1:]

        if self.topic == self.remote_action_flag:
            self.remote_actions = json.loads(msg.payload)
        else:
            self.payload = json.loads(msg.payload)

    def on_subscribe(self, client, obj, mid, granted_qos):
        print("Subscribed, QOS granted: " + str(granted_qos))

    def setup_mqtt(self):

        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_publish = self.on_publish
        self.mqttc.on_message = self.on_message
        self.mqttc.on_subscribe = self.on_subscribe

        self.mqttc.connect(self.url.hostname, self.url.port)

    def subscribe(self):
        self.mqttc.subscribe(self.base_topic + "/#", 0)

    def run(self):
        self.mqttc.loop_start()

    def publish(self, topic, message):
        self.call += 1
        json_massage = json.dumps(message)
        self.mqttc.publish(self.base_topic + "/" + topic, json_massage)


if __name__ == "__main__":
    b = Broker()
    b.run()
    b.subscribe()
    pprint(b.payload)
