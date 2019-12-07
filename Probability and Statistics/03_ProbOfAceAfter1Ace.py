"""Program to find the probability of drawing an ace after drawing an ace on the first draw"""
from fractions import Fraction as F
cards = 52        # total cards in total pack
aces = 4           # total ace cards
# after taking out  1 ace card
cards -= 1        # total cards reduced by 1
aces -= 1         # total ace cards will also reduce by 1
# Probability of favourable outcome in fraction
print(f'Probability of drawing an ace after drawing an ace in 1st draw: {F(aces, cards)}')
# Probability of favourable outcome in percentage
# print(f'Probability of drawing an ace after drawing an ace in 1st draw: {round(aces/cards, 4)*100} %')
