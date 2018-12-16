from manage import app
from web.main import main
from flask import render_template


@main.route('/')
def index():

    lights = light_status()

    return render_template('main/index.html', lights=lights)


def light_status():

    lights = []
    broker = app.broker

    for key in broker.payload.keys():
        light = broker.payload.get(key)
        lights.append([light['name'], light['status']])

    return lights
