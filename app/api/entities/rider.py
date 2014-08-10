from mongoengine import Document
from mongoengine.fields import StringField, IntField
import json

class Rider(Document):
    """I am a rider for the Disaster Relief Trials
    @attr: string name
    @attr: int number
    @attr: string bike_type
    @attr: string time ('HH:MM:SS')
    """
    name = StringField(max_length=255, required=True)
    number = IntField(required=True)
    bike_type = StringField(max_length=50)
    time = StringField(max_length=8)

    def to_dict(self):
        return {
            "name": self.name,
            "number": self.number,
            "bike_type": self.bike_type,
            "time": self.time
        }
