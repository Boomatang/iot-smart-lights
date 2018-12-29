from . import db


class Device(db.Model):
    __tablename__ = "devices"

    id = db.Column(db.Integer, primary_key=True)
    switches = db.relationship('Switches', backref='device')
    lights = db.relationship('Lights', backref='device')


class Switches(db.Model):
    __tablename__ = 'switches'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Lights(db.Model):
    __tablename__ = 'lights'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

