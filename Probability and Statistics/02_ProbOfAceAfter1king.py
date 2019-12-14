"""Program to find the probability of drawing an ace after drawing a king on the first draw"""
from fractions import Fraction
cards = 52        # total cards in total pack
aces = 4           # total ace cards
# after removing king in first draw
cards -= 1            # total cards will be reduced but aces will be the same
# showing probability in fraction
print(f'Probability of an ace from pack of cards after drawing king in 1st draw: {Fraction(aces, cards)}')
# showing probability in percentage
# print(f'Probability of an ace from pack of cards after drawing king in 1st draw: {round(aces/cards,4)*100} %')
