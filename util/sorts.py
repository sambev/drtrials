import operator


def sort_riders(riders):
    lengths = {}
    completed = 0

    for rider in riders:
        for time in rider['times']:
            if time['time'] != '':
                completed += 1

        lengths[rider['name']] = completed
        completed = 0

    sorted_lengths = sorted(lengths.items(), key=operator.itemgetter(1), reverse=True)
    sorted_riders = []

    for length in sorted_lengths:
        for rider in riders:
            if length[0] == rider['name']:
                sorted_riders.append(rider)

    return sorted_riders
