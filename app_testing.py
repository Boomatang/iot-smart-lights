from device.controller import Controller
from device.light import Light
from device.remote_light import RemoteLight
from device.switch import Switch

if __name__ == "__main__":
    device = Controller("Pi 1")

    device.add_switch(Switch("S1"))
    device.add_switch(Switch("S2"))
    device.add_switch(Switch("S3"))

    device.add_light(Light("L5"))
    device.add_light(Light("L6"))
    device.add_light(Light("L7"))
    device.add_light(RemoteLight("remote light"))
    device.add_remote_light_by_id('Sense Grid')

    device.configure_switch('S1', ['L5', 'L6'])
    device.configure_switch('S2', ['L7', 'remote light'])
    device.configure_switch('S3', ['Sense Grid'])

    s1 = device.switches.get("S1")
    s2 = device.switches.get("S2")
    s3 = device.switches.get("S3")

    l1 = device.lights.get('L5')
    l2 = device.lights.get('L6')
    l3 = device.lights.get('L7')
    r1 = device.lights.get('remote light')
    r2 = device.lights.get('Sense Grid')
