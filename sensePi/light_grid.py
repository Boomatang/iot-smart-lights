from device.light import Light


class LightGrid(Light):
    def __init__(self, id_tag, sense):
        Light.__init__(self, id_tag)
        self.sense = sense
        self.red = (255, 0, 0)

    def on(self):
        if not self.active:
            self.sense.clear(self.red)
            self.active = True

    def off(self):
        if self.active:
            self.sense.clear()
            self.active = False
