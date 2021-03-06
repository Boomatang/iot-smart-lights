from sense_hat import SenseHat

from device.controller import Controller
from sensePi.light_grid import LightGrid
from sensePi.push_button import PushButton


class SenseController(Controller):
    def __init__(self, id_tag):
        Controller.__init__(self, id_tag=id_tag)

        self.sense = SenseHat()
        self.setup()

    def setup(self):
        self.add_switch(PushButton('B1', self.sense))

        self.add_light(LightGrid('Sense Grid', self.sense))

        self.configure_switch('B1', ['Sense Grid'])

    def run(self):
        for switch in self.switches.keys():
            self.switches.get(switch).run()
            self.switches.get(switch).action()


if __name__ == "__main__":
    sensePi = SenseController('sensePi')

    sensePi.loop()
