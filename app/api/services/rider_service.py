from app.api.entities.rider import Rider
from mongoengine import connect

class RiderService(object):
    """I am the the public interface to the logic surrounding Rider
    """
    def __init__(self):
        try:
            self.con = connect('sf_drtrials')
        except Exception as e:
            print e.message
            print 'Unable to connect to Mongo.  Is it running?'

    def create_rider(self, data):
        """Create a new rider
        :param data - dict
        :return Rider object instance
        """
        new_rider = Rider(
            data['name'],
            data['number'],
            data['bike_type'],
        )
        new_rider.save()
        return new_rider

    def find_riders(self, id=None):
        """Find a rider giving the rider number
        :param id - int rider id
        :return mongoengine.queryset.QuerySet
        """
        if id:
            return Rider.objects(id=id)
        else:
            return Rider.objects().all()

    def update_rider(self, id, data):
        """Update the rider with the given id, create one if a rider doesn't
        exist.
        :param id - int rider id.
        :return Rider object instance
        """
        rider = self.find_riders(id)[0]
        rider.name = data['name']
        rider.number = data['number']
        rider.bike = data['bike_type']

        updated = rider.save()
        return updated

    def delete_rider(self, id):
        """Delete the rider with the given id
        :param id - int rider id
        :return response - dict as such:
            {
                'error': False
                'msg': 'Success'
            }
        """
        rider = self.find_riders(id)[0]
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
