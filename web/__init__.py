from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from device.broker import Broker

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    broker = Broker()
    app.broker = broker
    app.broker.run()
    app.broker.subscribe()
    app.broker.publish('status', {})

    return app
