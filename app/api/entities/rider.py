from mongoengine import EmbeddedDocument
from mongoengine.fields import StringField, IntField, EmbeddedDocumentField, \
    ListField
from app.api.entities.time import Time

class Rider(EmbeddedDocument):
    """I am a rider for the Disaster Relief Trials
    @attr: string name
    @attr: int number
    @attr: string bike_type
    @attr: string time ('HH:MM:SS')
    """
    name = StringField(max_length=255, required=True)
    number = IntField(required=True, unique=True)
    times = ListField(EmbeddedDocumentField(Time))
