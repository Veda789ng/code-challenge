from . import db

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String(15))
    date = db.Column(db.String(8))
    maximum_temperature = db.Column(db.Integer)
    minimum_temperature = db.Column(db.Integer)
    precipitation = db.Column(db.Integer)

    @property
    def serialize(self):
        return {
            "station": self.station,
            "date": self.date,
            "maximum_temperature": self.maximum_temperature,
            "minimum_temperature": self.minimum_temperature,
            "precipitation": self.precipitation,
        }

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String(15))
    date = db.Column(db.String(8))
    final_maximum_temperature = db.Column(db.Integer)
    final_minimum_temperature = db.Column(db.Integer)
    final_precipitation = db.Column(db.Integer)

    @property
    def serialize(self):
        return {
            "station": self.station,
            "date": self.date,
            "final_maximum_temperature": self.final_maximum_temperature,
            "final_minimum_temperature": self.final_minimum_temperature,
            "final_precipitation": self.final_precipitation,
        }