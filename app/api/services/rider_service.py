from app.api.entities.rider import Rider
from mongoengine import connect

class RiderService(object):
    """I am the the public interface to the logic surrounding Rider
    """
    def __init__(self):
        self.con = connect('sf_drtrials')

    def create_rider(self, data):
        """Create a new rider
        :param data - dict
        :return Rider object instance
        """
        new_rider = Rider(
            data['name'],
            data['number'],
            data['bike'],
            data['time']
        )
        return new_rider.save()

    def find_riders(self, number=None):
        """Find a rider giving the rider number
        :param number - int rider number.  If none, find all
        :return mongoengine.queryset.QuerySet
        """
        if number:
            return Rider.objects(number=number)
        else:
            return Rider.objects().all()

    def update_rider(self, number, data):
        """Update the rider with the given number, create one if a rider doesn't
        exist.
        :param number - int rider number.
        :return Rider object instance
        """
        rider = self.find_riders(number)[0]
        rider.name = data['name']
        rider.number = data['number']
        rider.bike = data['bike']
        rider.time = data['time']

        updated = rider.save()
        return updated

    def delete_rider(self, number):
        """Delete the rider with the given number
        :param number - int rider number
        :return response - dict as such:
            {
                'error': False
                'msg': 'Success'
            }
        """
        rider = self.find_riders(number)[0]
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
