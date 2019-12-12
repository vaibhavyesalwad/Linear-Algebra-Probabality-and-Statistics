"""X is a normally normally distributed variable with mean μ = 30 and standard deviation σ = 4.
 Write a program to find
a. P(x < 40)
b. P(x > 21)
c. P(30 < x < 35)
"""
# cumulative probability is sum of probabilities of the data points <= given data point
# using z-table that gives cumulative probability for given +ve z-score
# for -ve z-scores it is (1 - (cumulative probability for absolute value of z-score))
z_score = lambda x: (x-mean)/std_deviation    # anonymous fn for calculating z-score for given data point

mean = 30
std_deviation = 4

# calculating probability of x < 40
print(f'Z-score for 40: {z_score(40)}')
print('P (x < 40): 0.9938')       # cumulative probability for z-score 2.5 is 0.9938

# calculating probability of x > 21
print(f'Z-score for 21: {z_score(21)}')
print('P (x > 21): 0.9878')       # cumulative probability for z-score 2.25 is 0.9878 using only positive z-scores

# calculating probability of 30 < x < 35
print(f'Z-score for 35: {z_score(35)}')         # cumulative probability for z-scores 1.25 is 0.8944
print(f'Z-score for 30: {z_score(30)}')         # cumulative probability for z-scores 0.00 is 0.5
print(f'P (30 < x < 35): {0.8944-0.5}')         # resultant probability
