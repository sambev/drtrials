from app.api.entities.race import Race
from mongoengine import connect

class RaceService(object):
    """I am the the public interface to the logic surrounding Race
    """
    def __init__(self):
        try:
            self.con = connect('sf_drtrials')
        except Exception as e:
            print e.message
            print 'Unable to connect to Mongo.  Is it running?'

    def create_race(self, data):
        """Persist a Race to the database
        :param - data dict race data
        :example:
            {
                'name': 'Foobar',
                'time': '00:23:20'
            }
        """
        new_race = Race(
            data.get('name'),
            data.get('time')
        )

        new_race.save()

        return new_race
