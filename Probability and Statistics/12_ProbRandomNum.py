"""Program to find the probability of getting a random number from the interval [2, 7]"""

from fractions import Fraction
numbers = [2, 3, 4, 5, 6, 7]
print(f'P (random number in [2,7]): {Fraction(1, len(numbers))}')       # probability of getting random number


