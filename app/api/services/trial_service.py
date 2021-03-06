from mongoengine import connect
from app.api.entities.trial import Trial
from app.api.services.rider_service import RiderService

class TrialService(object):
    """I am the the public interface to the logic surrounding Trial
    """
    def __init__(self):
        self.rider_service = RiderService()
        try:
            self.con = connect('sf_drtrials')
        except Exception as e:
            print e.message
            print 'Unable to connect to Mongo.  Is it running?'

    def create(self, data):
        """Persist a Trial to the database
        :param - data {dict} trial data
        """
        new_trial = Trial(
            data.get('city'),
            data.get('races'),
        )

        new_trial.save()

        return new_trial

    def find(self, id=None):
        """Find a trial either by it's id or find all
        :param {string} id
        """
        if id:
            return Trial.objects(id=id)
        else:
            return Trial.objects().all()

    def update(self, id, data):
        """Update the trial with the given id, create one if a trial doesn't
        exist.
        :param {string} id trial id.
        :param {data} dict representation of the trial
        :return {app.api.entities.Trial}
        """
        trial = self.find(id)[0]
        trial.city = data.get('city')
        trial.races = data.get('races')
        riders = []
        # we don't actually update the riders, we just overwrite them
        if data.get('riders'):
            for rider in data['riders']:
                riders.append(self.rider_service.create(rider, trial.races))

        trial.riders = riders

        updated = trial.save()
        return updated

    def delete(self, id):
        """Delete the trial with the given id
        :param id - int trial id
        """
        trial = self.find(id)[0]
        try:
            trial.delete()
            return {
                'error': False,
                'msg': 'Deleted'
            }
        except Exception as e:
            return {
                'error': True,
                'msg': str(e)
            }
