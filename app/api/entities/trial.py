from mongoengine import Document
from mongoengine.fields import StringField, ListField, DateTimeField
import datetime

class Trial(Document):
    """I represent a trial in a given city
    @attr: string city
    @attr: list races - list of race names
    """
    city = StringField(max_length=255, required=True, unique=True)
    races = ListField(required=True)
    date = DateTimeField(default=datetime.datetime.now)
