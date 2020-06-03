import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    siuits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.siuits
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')
print (beer_card)

deck = FrenchDeck()
print(len(deck))

print(deck[0])
print(deck[-1])
print('-------random cards-----')
print(choice(deck))
print(choice(deck))
print('------card selection----')
print(deck[:3])
print(deck[12::13])
print('-------card iteration---------')
for card in deck:
    print(card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
print("---sorted by value----")
for card in sorted(deck, key=spades_high):
    print(card)