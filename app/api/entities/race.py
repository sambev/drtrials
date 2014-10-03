from mongoengine import EmbeddedDocument
from mongoengine.fields import StringField, DateTimeField
import datetime

class Race(EmbeddedDocument):
    """I am a race for a given Rider
    @attr: string name
    @attr: datetime time - the bikers time (default:None)
    """
    name = StringField(max_length=255, required=True)
    time = StringField()
