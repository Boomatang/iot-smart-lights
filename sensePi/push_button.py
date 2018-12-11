import time

from device.switch import Switch


class PushButton(Switch):
    def __init__(self, id_tag, sense):
        Switch.__init__(self, id_tag)
        self.sense = sense

        # For set up checking
        self.green = (0, 255, 0)
        self.sense.clear(self.green)
        time.sleep(1)
        self.sense.clear()

    def run(self):
        self.sense.stick.direction_middle = self.change_color

    def change_color(self, event):
        print(event)
        if event.action == 'pressed' and not self.start:
            self.start = True
        elif event.action == 'pressed' and self.start:
            self.start = False

