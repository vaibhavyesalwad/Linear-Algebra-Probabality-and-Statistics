"""In my town, it's rainy 1/3 of the days. Given that it is rainy, there will be heavy traffic with
probability 1/2, and given that it is not rainy, there will be heavy traffic with probability 1/4.
If it's rainy and there is heavy traffic, I arrive late for work with probability 1/2. On the other hand,
the probability of being late is reduced to 1/8 if it is not rainy and there is no heavy traffic.
In other situations (rainy and no traffic, not rainy and traffic) the probability of being late is 0.25.
You pick a random day.
1. Probability that it's not raining and there is heavy traffic and I am not late
2. Probability that I am late?
3 .Given that I arrived late at work, what is the probability that it rained that day
"""
from fractions import Fraction
p_rain = Fraction(1, 3)           # probability of day is rainy
p_rain_traffic = Fraction(1, 2)       # probability of heavy traffic after rain
p_noRain_traffic = Fraction(1, 4)     # probability of heavy traffic after no rain
# probability of getting late after rain followed by heavy traffic
p_rain_traffic_late = Fraction(1, 2)
# if no rain followed by no heavy traffic
p_noRain_noTraffic_late = Fraction(1, 8)
# other remaining conditions not rainy followed by heavy traffic and rain followed by no heavy traffic
p_rain_noTraffic_late = p_noRain_traffic_late = Fraction(1, 4)

# probability of not late after earlier conditions is found by multiplying all prior probabilities to be encountered
result = (1-p_rain) * p_noRain_traffic * (1-p_noRain_traffic_late)
print(f'P (NOT getting late when NO rain followed by heavy traffic): {result}')
# adding all conditions for getting late i.e four conditions for being late
cond1 = p_rain*p_rain_traffic*p_rain_traffic_late
cond2 = p_rain*(1-p_rain_traffic)*p_rain_noTraffic_late
cond3 = (1-p_rain)*p_noRain_traffic*p_noRain_traffic_late
cond4 = (1-p_rain)*(1-p_noRain_traffic)*p_noRain_noTraffic_late
all_late = cond1 + cond2 + cond3 + cond4
print(f'P (getting late in all situations): {all_late}')
# probability of it rained given I'm late
print(f"P (it rained / I'm late): {(cond1+ cond2)/all_late}")


