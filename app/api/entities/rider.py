from mongoengine import Document
from mongoengine.fields import StringField, IntField, EmbeddedDocumentField, \
    ListField
from app.api.entities.race import Race

class Rider(Document):
    """I am a rider for the Disaster Relief Trials
    @attr: string name
    @attr: int number
    @attr: string bike_type
    @attr: string time ('HH:MM:SS')
    """
    name = StringField(max_length=255, required=True)
    number = IntField(required=True, unique=True)
    bike_type = StringField(max_length=50)
    races = ListField(EmbeddedDocumentField(Race))
