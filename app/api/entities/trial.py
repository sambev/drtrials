from mongoengine import Document
from mongoengine.fields import StringField, ListField, DateTimeField, \
    EmbeddedDocumentField
from app.api.entities.rider import Rider
import datetime

class Trial(Document):
    """I represent a trial in a given city
    @attr: string city
    @attr: list races - list of race names
    """
    city = StringField(max_length=255, required=True, unique=True)
    races = ListField()
    riders = ListField(EmbeddedDocumentField(Rider))
    date = DateTimeField(default=datetime.datetime.now)
