"""Program to find probability of drawing an ace from pack of cards"""
from fractions import Fraction        # using fractions module
cards = 52        # total cards in total pack
aces = 4           # total ace cards
print(f'Probability of an ace from pack of cards: {Fraction(aces, cards)}')       # representing probability in fraction
# print(f'Probability if of an ace: {round(aces/cards,2)}') # representing probability in floats
