"""A fair coin is tossed three times write a program to find
1. Probability of three heads, HHH
2. Probability of exactly one head
3. Probability of at least one heads
4. Probability of at least two heads"""

from itertools import product
from fractions import Fraction
sides = {'H', 'T'}               # set sides of coin
# finding total outcomes than can occur i.e.  sample space
sample_space = list(product(sides, sides, sides))   # we are using cartesian product as coin tossed 3 times
# we have used cartesian product as itertools module don't have permutations with replacement fn
print(f'Sample space: {sample_space}')   # sample space for tossing 3 coins

# using generator expression to count total required conditions
favourable = sum(result.count('H') == 3 for result in sample_space)         # for exactly 3 heads
print(f'P (exactly 3 heads): {Fraction(favourable, len(sample_space))}')     # Probability in fraction

favourable = sum(result.count('H') == 1 for result in sample_space)         # for exactly 1 head
print(f'P (exactly 1 head): {Fraction(favourable, len(sample_space))}')  # Probability in fraction

favourable = sum(result.count('H') >= 1 for result in sample_space)           # for at least 1 head
print(f'P (at least 1 head): {Fraction(favourable, len(sample_space))}')  # Probability in fraction

favourable = sum(result.count('H') >= 2 for result in sample_space)            # for at least 2 heads
print(f'P (at least 2 heads): {Fraction(favourable, len(sample_space))}')  # Probability in fraction
