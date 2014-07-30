class Rider(object):
    """I am a rider for the Disaster Relief Trials
    @attr: string name
    @attr: int number
    @attr: string bike_type?
    @attr: int score?
    """

    def __init__(self, name, number, bike, score):
        self.name = name
        self.number = number
        self.bike = bike
        self.score = score
