
from device.controller import Controller
import RPi.GPIO as gpio

from device.remote_light import RemoteLight
from gpioPi.gpio_light import GpioLight
from gpioPi.gpio_switch import GpioSwitch


class GpioController(Controller):

    def __init__(self, id_tag):
        Controller.__init__(self, id_tag=id_tag)
        self.setup()

    def setup(self):
        gpio.setmode(gpio.BCM)

        self.add_light(GpioLight('yellow light', 2))
        self.add_light(GpioLight('green light', 4))
        self.add_light(RemoteLight('Sense Grid'))

        self.add_switch(GpioSwitch("GPIO Switch 1", (14, 15)))
        self.add_switch(GpioSwitch("GPIO Switch 2", (17, 18)))
        self.add_switch(GpioSwitch("GPIO Switch 3", (23, 24)))

        self.configure_switch('GPIO Switch 1', ['yellow light'])
        self.configure_switch('GPIO Switch 2', ['green light'])
        self.configure_switch('GPIO Switch 3', ['Sense Grid'])

    def run(self):
        for switch in self.switches.keys():
            self.switches.get(switch).run()

    def loop(self):
        while True:
            self.run()


if __name__ == "__main__":
    gpio_pi = GpioController("Gpio PI")
    gpio_pi.loop()
