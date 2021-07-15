import itertools as it
import random


def shuffle(deck):
    """Return iterator over shuffled deck."""
    deck = list(deck)
    random.shuffle(deck)
    return iter(tuple(deck))


def cut(deck, n):
    """Return an iterator over a deck of cards cut at index `n`."""
    if n < 0:
        raise ValueError('`n` must be a non-negative integer')

    deck = list(deck)
    return iter(deck[n:] + deck[:n])


# with itertools

def cut_wit_itertools(deck, n):
    """Return an iterator over a deck of cards cut at index `n`."""
    deck1, deck2 = it.tee(deck, 2)
    top = it.islice(deck1, n)
    bottom = it.islice(deck2, n, None)
    return it.chain(bottom, top)


'''
You start by creating a list of hand_size references to an iterator over deck.
You then iterate over this list, removing num_hands cards at each step and storing them in tuples.

Next, you zip() these tuples up to emulate dealing one card at a time to each player.
This produces num_hands tuples, each containing hand_size cards.
Finally, you package the hands up into a tuple to return them all at once.
'''


def deal(deck, num_hands=1, hand_size=5):
    iters = [iter(deck)] * hand_size
    return tuple(zip(*(tuple(it.islice(itr, num_hands)) for itr in iters)))


'''
>>> p1_hand, p2_hand, p3_hand = deal(cards, num_hands=3)
>>> p1_hand
(('A', 'S'), ('5', 'S'), ('7', 'H'), ('9', 'H'), ('5', 'H'))
>>> p2_hand
(('10', 'H'), ('2', 'D'), ('2', 'S'), ('J', 'C'), ('9', 'C'))
>>> p3_hand
(('2', 'C'), ('Q', 'S'), ('6', 'C'), ('Q', 'H'), ('A', 'C'))
>>> len(tuple(cards))
37
'''


def main():
    ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    suits = ['♥', '♦', '♣', '♠']

    cards = it.product(ranks, suits)
    cards = shuffle(cards)

    cards = cut(cards, 26)  # Cut the deck in half.


if __name__ == '__main__':
    main()
