
class Controller:
    def __init__(self, id_tag):
        self.id = id_tag
        self.switches = {}
        self.lights = {}

        self.system_lights_status = {}
        # {'l1': [0, 1],  'l1' is off and needs to be turned on
        #  'l2': [1, None],     'l2' is on, no action required
        #  'l3': [1, 0]}  'l3' is on and needs to be turned off

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

    def update_local_light_status(self):
        old_status = self.system_lights_status.copy()
        for light in self.lights.keys():
            if light in self.system_lights_status.keys():
                self.system_lights_status[light][0] = self.lights[light].is_on()
            else:
                self.system_lights_status.setdefault(light, [0, None])
                self.system_lights_status[light][0] = self.lights[light].is_on()
        added, removed, modified, same = dict_compare(old_status, self.system_lights_status)

        # print("added : " + str(len(added)))
        # print("removed : " + str(len(removed)))
        # print("modified : " + str(len(modified)))
        # print("same : " + str(len(same)))

        if len(modified):
            self.publish()

    def publish(self):
        print("published change")

    def run(self):
        # TODO I don't think this should run this often
        self.update_local_light_status()

    def __repr__(self):
        return "<Controller ID : " + self.id + ">"

    def loop(self):
        while True:
            self.run()


def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o: (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same
