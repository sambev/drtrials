from mongoengine import connect
from app.api.entities.trial import Trial

class TrialService(object):
    """I am the the public interface to the logic surrounding Trial
    """
    def __init__(self):
        try:
            self.con = connect('sf_drtrials')
        except Exception as e:
            print e.message
            print 'Unable to connect to Mongo.  Is it running?'

    def create_trial(self, data):
        """Persist a Trial to the database
        :param - data dict trial data
        :example:
            {
                'city': 'Seattle',
                'races': [
                    'race1',
                    'race2',
                    'race3'
                ]
                'date': '2014-08-24 08:23:14'
            }
        """
        new_trial = Trial(
            data.get('city'),
            data.get('races'),
        )

        new_trial.save()

        return new_trial

    def find_trial(self, id=None):
        """Find a trial either by it's id or find all
        :param id - id of the trial
        """
        if id:
            return Trial.objects(id=id)
        else:
            return Trial.objects().all()

    def update_trial(self, id, data):
        """Update the trial with the given id, create one if a trial doesn't
        exist.
        :param id - int trial id.
        :return trial object instance
        """
        trial = self.find_trial(id)[0]
        trial.city = data.get('city')
        trial.time = data.get('time')

        updated = trial.save()
        return updated

    def delete_trial(self, id):
        """Delete the trial with the given id
        :param id - int trial id
        :return response - dict as such:
            {
                'error': False
                'msg': 'Success'
            }
        """
        trial = self.find_trial(id)[0]
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
