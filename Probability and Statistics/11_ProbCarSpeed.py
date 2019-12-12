""" A radar unit is used to measure speeds of cars on a motorway. The speeds are normally distributed
with a mean of 90 km/hr and a standard deviation of 10 km/hr. Write a program to find the probability
that a car picked at random is travelling at more than 100 km/hr"""
# z-table gives cumulative probability for given z-score and it is sum of probabilities for points <= given data point
mean = 90
std_deviation = 10
x = 100       # random variable
z_score = (x - mean)/std_deviation        # formulae for z-score
# calculating probability that picked car speed > 100
print(f'Z-score for {x}: {z_score}')
print(f'P (speed > 100): {1- 0.8413}')      # cumulative probability for z-score 1.0 is 0.8413 for speed < 100

