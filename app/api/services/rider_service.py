from mongoengine import connect
from app.api.entities.rider import Rider
from app.api.entities.time import Time
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

    def create(self, data, races):
        """Create a new rider
        :param {data} - dict
        :param {list<String>} - races
        :return Rider object instance
        """
        new_rider = Rider(
            name=data.get('name'),
            number=data.get('number')
        )

        # XXX This is pretty ugly and convoluted logic, clean it up and test it
        if data.get('times'):
            times = []
            for time in data.get('times'):
                times.append(Time(name=time.get('name'), time=time.get('time')))

            for race in races:
                if race not in [time.name for time in times]:
                    times.append(Time(name=race))

            new_rider.times = times
        else:
            new_rider.times = [Time(name=race) for race in races]

        return new_rider
