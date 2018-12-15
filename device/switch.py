class Switch:

    def __init__(self, id_tag):
        self.id = id_tag
        self.lights = []
        self.start = None

    def on(self):
        for light in self.lights:
            light.on()

    def off(self):
        for light in self.lights:
            light.off()

    def add_light(self, light):
        self.lights.append(light)

    def remove_light(self, light):
        self.lights.remove(light)

    def action(self):
        if self.start:
            self.on()
            self.start = None
        elif self.start is False:
            self.off()
            self.start = None
        else:
            pass

    def run(self):
        print("run like the wind")

    def __repr__(self):
        return "<Switch ID : " + self.id + ">"
