from device.controller import Controller
from device.light import Light
from device.switch import Switch

if __name__ == "__main__":
    device = Controller("Pi 1")

    device.add_switch(Switch("base switch"))
    device.add_light(Light("remote light"))

    device.configure_switch('base switch', ['remote light'])

    s1 = device.switches.get("base switch")

    l1 = device.lights.get('remote light')
