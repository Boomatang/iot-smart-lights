from device.broker import Broker


class Light(Broker):
    def __init__(self, id_tag):
        Broker.__init__(self)
        self.run()
        self.subscribe()
        self.id = id_tag
        self.active = False
        self.status_flag = "status"
        self.action_flag = "action"

        # self.publish(self.status_flag, {})
        self.setup_network_devices()

    def on(self):
        print(self.id + ' is on')
        self.active = True
        self.reset_action()
        self.update_device_status()

    def off(self):
        print(self.id + ' is off')
        self.active = False
        self.reset_action()
        self.update_device_status()

    def is_on(self):
        return self.active

    def on_message(self, client, obj, msg):
        Broker.on_message(self, client, obj, msg)

        if self.topic == self.status_flag:
            self.action()

        if self.topic == self.action_flag:
            self.action()
            message = self.payload.get(self.id)

            if message['action'] is not None:
                self.act_on_light(message['action'])

    def action(self):
        print('I did stuff, ' + self.__repr__())
        self.setup_network_devices()
        self.update_device_status()

    def update_device_status(self):
        message = self.payload.get(self.id)
        if message["status"] != self.active and message['action'] is None:
            message["status"] = self.active
            self.update_network_status()

    def act_on_light(self, action):
        if action:
            self.on()
        else:
            self.off()

    def reset_action(self):
        print("reset act was called")
        message = self.payload.get(self.id)
        if message['action'] is not None:
            message['action'] = None
            print(message['action'])

    def update_network_status(self):
        self.publish(self.status_flag, self.payload)

    def setup_network_devices(self):
        if self.id not in self.payload.keys():
            self.payload.setdefault(self.id, {"status": self.is_on(), "action": None, "name": self.id})
            self.publish(self.status_flag, self.payload)
            print("Update status")

    def __repr__(self):
        return "<Light ID : " + self.id + ">"
