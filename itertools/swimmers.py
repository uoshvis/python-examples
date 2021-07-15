from collections import namedtuple
import csv
import datetime
import itertools as it
import statistics


class Event(namedtuple('Event', ['stroke', 'name', 'time'])):
    __slots__ = ()
    # for min()
    def __lt__(self, other):
        return self.time < other.time


def sort_and_group(iterable, key=None):
    """Group sorted `iterable` on `key`."""
    return it.groupby(sorted(iterable, key=key), key=key)


def grouper(iterable, n, fillvalue=None):
    iters = [iter(iterable)] * n
    return it.zip_longest(*iters, fillvalue=fillvalue)


def read_events(csvfile, _strptime=datetime.datetime.strptime):
    def _median(times):
        return statistics.median((_strptime(time, '%M:%S:%f').time()
                                  for time in row['Times']))

    fieldnames = ['Event', 'Name', 'Stroke']
    with open(csvfile) as infile:
        # reads each row in the swimmers.csv file into an OrderedDict object
        # By assigning the 'Times' field to restkey,
        # the “Time1”, “Time2”, and “Time3” columns of each row in the CSV file will be stored
        # in a list on the 'Times' key
        reader = csv.DictReader(infile, fieldnames=fieldnames, restkey='Times')
        next(reader)  # Skip header.
        for row in reader:
            yield Event(row['Stroke'], row['Name'], _median(row['Times']))


def main():
    # a tuple of Event objects is created
    events = tuple(read_events('swimmers.csv'))
    #  create a for loop that iterates over the data in the events tuple grouped by stroke
    for stroke, evts in sort_and_group(events, key=lambda evt: evt.stroke):
        # group the evts iterator by swimmer name
        events_by_name = sort_and_group(evts, key=lambda evt: evt.name)
        # calculate the best time for each swimmer in events_by_name
        best_times = (min(evt) for _, evt in events_by_name)
        # sort best_times by time and aggregate the result into groups of four
        sorted_by_time = sorted(best_times, key=lambda evt: evt.time)
        # use the grouper() function use islice() to grab the first two groups.
        teams = zip(('A', 'B'), it.islice(grouper(sorted_by_time, 4), 2))
        #  teams is an iterator over exactly two tuples representing the “A” and the “B” team for the stroke.
        #  The first component of each tuple is the letter “A” or “B”,
        #  and the second component is an iterator over Event objects containing the swimmers in the team

        for team, swimmers in teams:
            print('{stroke} {team}: {names}'.format(
                stroke=stroke.capitalize(),
                team=team,
                names=', '.join(swimmer.name for swimmer in swimmers)
            ))


if __name__ == '__main__':
    main()
