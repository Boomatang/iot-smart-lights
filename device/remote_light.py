from device.broker import Broker


class RemoteLight(Broker):

    def __init__(self, remote_id):
        Broker.__init__(self)
        self.id = remote_id
        self.act = True
        self.remote_action_flag = 'remote action'

        self.state = {self.id: {'action': None}}

    def on(self):
        print("Turning on remote light")
        self.payload_action(True)

    def off(self):
        print("Turning off remote light")
        self.payload_action(False)

    def payload_action(self, action):
        current = self.state.get(self.id)
        current['action'] = action

        print("sent update")
        self.publish(self.remote_action_flag, self.state)
        self.act = False

    def __repr__(self):
        return "<Remote Light ID : " + self.id + ">"
