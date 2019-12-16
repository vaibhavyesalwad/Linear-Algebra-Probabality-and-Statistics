"""A bank teller serves customers standing in the queue one by one. Suppose that the service time Xi
for customer i has mean E(Xi)=2 (minutes) and Var(Xi)=1. We assume that service times for different bank
customers are independent. Let Y be the total time the bank teller spends serving 50 customers.
Write a program to find P(90<Y<110)"""
from math import sqrt
# X be time given to a customer
mean_Xi = 2    # given
variance_Xi = 1  # given
# Total time is Y be total time
mean_Yi = 2 * 50      # total 50 customers so 100 minutes mean for total time
variance_Yi = 1 * 50  # variance for total time
# we want std deviation for calculation
std_deviation_Yi = sqrt(variance_Yi)      # variance  = std_deviation ** 2

# calculating z-score for given data points
z_score = lambda x: (x - mean_Yi)/std_deviation_Yi
# for first condition total time = 90 minutes i.e. Y = 90
z1 = z_score(90)
print(f'Z-score for total time 90 minutes: {z1}')
print(f'P (Y < 90): {0.0793}')

# for second condition total time = 110 minutes i.e. Y = 110
z2 = z_score(110)
print(f'Z-score for total time 110 minutes: {z2}')
print(f'P (Y < 110): { 0.9207}')

# calculating required probability
print(f'P (90 < Y < 110): {0.9207 - 0.0793}')