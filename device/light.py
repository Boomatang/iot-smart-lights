class Light:
    def __init__(self, id_tag):
        self.id = id_tag
        self.switched = False
        self.active = False

    def on(self):
        print(self.id + ' is on')
        self.switched = True

    def off(self):
        print(self.id + ' is off')
        self.switched = False

    def __repr__(self):
        return "<Light ID : " + self.id + ">"
