from device.switch import Switch
import RPi.GPIO as gpio


class GpioSwitch(Switch):
    def __init__(self, id_tag, pins):
        Switch.__init__(self, id_tag=id_tag)
        self.pins = pins
        self.current_pin = 0
        self.active = False
        self.setup()

    def setup(self):
        for pin in self.pins:
            gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
            if gpio.input(pin):
                self.current_pin = pin
                print("Setup set current pin to : " + str(self.current_pin))

    def check_input(self):
        if gpio.input(self.current_pin) == 0:
            print("Switch was flipped, pin: " + str(self.current_pin))
            for pin in self.pins:
                if gpio.input(pin) and not self.active:
                    self.start = True
                    self.active = True
                    self.current_pin = pin

                elif gpio.input(pin) and self.active:
                    self.start = False
                    self.active = False
                    self.current_pin = pin

    def run(self):
        self.check_input()
        self.action()
