# all of the code below is brought to you by iffy
# https://github.com/iffy
def sortableTime(x):
    if not x:
        return (0,0)
    return [(-int(a[0]), -int(a[1])) for a in x.split(':')]


def sort_riders(riders):
    def sortkey(rider):
        num_nonzero_times = len(filter(None, [x['time'] for x in rider['times']]))
        times = [sortableTime(x['time']) for x in rider['times']][::-1]
        key = tuple([num_nonzero_times] + times)
        return key
    return sorted(riders, key=sortkey, reverse=True)
