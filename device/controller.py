from device.light import Light
from device.switch import Switch


class Controller:
    def __init__(self, id_tag):
        self.id = id_tag
        self.switches = {}
        self.lights = {}

    def add_switch(self, switch):
        self.switches[switch.id] = switch

    def add_light(self, light):
        self.lights[light.id] = light

    def setup(self):
        print('No set up done')

    def configure_switch(self, switch_id, light_ids):
        if switch_id in self.switches.keys():
            switch = self.switches.get(switch_id)

            for light_id in light_ids:
                if light_id in self.lights.keys():
                    switch.add_light(self.lights.get(light_id))

    def __repr__(self):
        return "<Controller ID : " + self.id + ">"



