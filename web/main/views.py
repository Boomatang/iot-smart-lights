from manage import app
from web.main import main
from flask import render_template, flash, url_for, redirect


@main.route('/')
def index():

    lights = light_status()

    return render_template('main/index.html', lights=lights)


@main.route('/<id_tag>/<state>')
def act_on_lights(id_tag, state):

    if state == 'on':
        light_action(id_tag, True)
        flash("Please wait, light is been turned on")
    elif state == 'off':
        light_action(id_tag, False)
        flash("Please wait, light is been turned off")
    else:
        flash("Invalid path")

    return redirect(url_for('.index'))


def light_status():

    lights = []
    broker = app.broker

    for key in broker.payload.keys():
        light = broker.payload.get(key)
        lights.append([light['name'], light['status'], key])

    return lights


def light_action(id_tag, action):
    state = {id_tag: {'action': action}}

    print("sent update")
    app.broker.publish('remote action', state)
