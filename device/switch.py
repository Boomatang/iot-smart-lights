class Switch:

    def __init__(self, id_tag):
        self.id = id_tag
        self.lights = []

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

    def __repr__(self):
        return "<Switch ID : " + self.id + ">"
