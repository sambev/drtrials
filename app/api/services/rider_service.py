from mongoengine import connect
from app.api.entities.rider import Rider
from app.api.entities.race import Race
from app.api.entities.trial import Trial


class RiderService(object):
    """I am the the public interface to the logic surrounding Rider
    """
    def __init__(self):
        try:
            self.con = connect('sf_drtrials')
        except Exception as e:
            print e.message
            print 'Unable to connect to Mongo.  Is it running?'

    def create(self, data):
        """Create a new rider
        :param data - dict
        :return Rider object instance
        """
        trial = Trial.objects(city='San Fransisco')[0]
        races = [Race(name=race) for race in trial.races]

        new_rider = Rider(
            name=data.get('name'),
            number=data.get('number'),
            bike_type=data.get('bike_type'),
            races=races
        )
        new_rider.save()

        return new_rider

    def find(self, id=None):
        """Find a rider giving the rider number
        :param id - int rider id
        :return dict
        """
        if id:
            return Rider.objects(id=id)
        else:
            return Rider.objects().all()

    def update(self, id, data):
        """Update the rider with the given id, create one if a rider doesn't
        exist.
        :param id - int rider id.
        :return Rider object instance
        """
        rider = self.find(id)[0]
        rider.name = data.get('name')
        rider.number = data.get('number')
        rider.bike = data.get('bike_type')
        races = data.get('races')
        rider.races = [Race(name=race['name'], time=race['time']) for race in races]

        updated = rider.save()
        return updated

    def delete(self, id):
        """Delete the rider with the given id
        :param id - int rider id
        :return response - dict as such:
            {
                'error': False
                'msg': 'Success'
            }
        """
        rider = self.find(id)[0]
        try:
            rider.delete()
            return {
                'error': False,
                'msg': 'Deleted'
            }
        except Exception as e:
            return {
                'error': True,
                'msg': str(e)
            }
