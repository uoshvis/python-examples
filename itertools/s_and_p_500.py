from collections import namedtuple
import csv
from datetime import datetime
import itertools as it
import functools as ft


class DataPoint(namedtuple('DataPoint', ['date', 'value'])):
    __slots__ = ()

    def __le__(self, other):
        return self.value <= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

'''
repeat() keeps returning a pointer to an iterator over the sequence argument,
which is being partially consumed at each iteration by the call to tuple() in the yield statement
'''


def consecutive_positives(sequence, zero=0):
    def _consecutives():
        for itr in it.repeat(iter(sequence)):
            yield tuple(it.takewhile(lambda p: p > zero,
                                     it.dropwhile(lambda p: p <= zero, itr)))
    return it.takewhile(lambda t: len(t), _consecutives())

# Read data from the CSV file and
# transform it into a sequence gains of daily percent changes using the “Adj Close” column.


def read_prices(csvfile, _strptime=datetime.strptime):
    with open(csvfile) as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            yield DataPoint(date=_strptime(row['Date'], '%Y-%m-%d').date(),
                            value=float(row['Adj Close']))


def main():
    # Read prices and calculate daily percent change.
    prices = tuple(read_prices('SP500.csv'))
    # prices needs to be transformed to a sequence of daily percent changes
    gains = tuple(DataPoint(day.date, 100*(day.value/prev_day.value - 1.))
                  for day, prev_day in zip(prices[1:], prices))

    # Find maximum daily gain/loss.
    zdp = DataPoint(None, 0)  # zero DataPoint
    max_gain = ft.reduce(max, it.filterfalse(lambda p: p <= zdp, gains), zdp)
    max_loss = ft.reduce(min, it.filterfalse(lambda p: p > zdp, gains), zdp)

    # Transform gains into a sequence growth_streaks of tuples of consecutive positive values in gains.
    # Find longest growth streak.
    growth_streaks = consecutive_positives(gains, zero=DataPoint(None, 0))
    # Determine the length of the longest tuple in growth_streaks and the beginning and ending dates of the streak.
    longest_streak = ft.reduce(lambda x, y: x if len(x) > len(y) else y,
                               growth_streaks)

    # Display results.
    print('Max gain: {1:.2f}% on {0}'.format(*max_gain))
    print('Max loss: {1:.2f}% on {0}'.format(*max_loss))

    print('Longest growth streak: {num_days} days ({first} to {last})'.format(
        num_days=len(longest_streak),
        first=longest_streak[0].date,
        last=longest_streak[-1].date
    ))


if __name__ == '__main__':
    main()
