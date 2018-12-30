from device.light import Light
import RPi.GPIO as gpio


class GpioLight(Light):
    def __init__(self, id_tag, pin):
        Light.__init__(self, id_tag=id_tag)
        self.pin = pin

        self.setup()

    def setup(self):
        gpio.setup(self.pin, gpio.OUT)
        gpio.output(self.pin, False)

    def on(self):
        self.reset_action()
        if not self.active:
            gpio.output(self.pin, True)
            self.active = True
            self.action()

    def off(self):
        self.reset_action()
        if self.active:
            gpio.output(self.pin, False)
            self.active = False
            self.action()
