"""The data shows the heights in inches and the pulse rates in beats per minute, for 9 people.
Write a program to find the correlation coefficient and interpret your result"""
from math import sqrt
heights = [68, 72, 65, 70, 62, 75, 78, 64, 68]
pulse_rates = [90, 85, 88, 100, 105, 98, 70, 65, 72]
total = len(heights)   # total records

# uncomment following multi-line comment for user inputs for heights & pulse_rates
'''
# taking number of records want to  input
while True:
    try:
        total = int(input('Enter total records you want to input:'))   # total records
        assert total > 0
        break
    except (ValueError, AssertionError):
        print('Please enter only integers > 0')

# taking values from user
heights = []
pulse_rates = []
for index in range(total):
    while True:
        try:
            height = int(input(f'Enter height(in inches) for person{index + 1}:'))
            pulse_rate = int(input(f'Enter pulse rate(in bpm) for person{index + 1}:'))
            # making sure inputs are valid for given variable
            assert 22 <= height <= 108 and 28 <= pulse_rate <= 200            
            heights.append(height)
            pulse_rates.append(pulse_rate)
            break
        except (ValueError, AssertionError):
            print('Please provide correct integer values for 22 inches <= height <= 108 inches '
                  '& 28 bpm <= pulse_rate <= 200 bpm')
'''

print('  Height     Pulse rate')
print('(in inches)   (in bpm) ')
# displaying given data
for index in range(total):
    print(f'   {heights[index]}           {pulse_rates[index]}')

# calculating product of height & pulse rate in each record
products = [heights[index] * pulse_rates[index] for index in range(total)]

# calculating square of each height & storing them same for pulse rates
sqr_heights = [height*height for height in heights]
sqr_pulse_rates = [pulse_rate*pulse_rate for pulse_rate in pulse_rates]

# finding correlation coefficient r
numerator = total * sum(products) - sum(heights) * sum(pulse_rates)
denominator = sqrt((total * sum(sqr_heights) - sum(heights) ** 2) * (total * sum(sqr_pulse_rates) - sum(pulse_rates) ** 2))
r = numerator/denominator

# displaying result
print(f'Correlation coefficient(r) between height & pulse rate: {r}')

if r == 1:
    print('Perfect positive relationship')
elif r == -1:
    print('Perfect negative relationship')
elif -0.2 <= r <= 0.2:
    print('Weak relationship')
elif r >= 0.75:
    print('Positive strong relationship')
elif r <= -0.75:
    print('Negative strong relationship')
else:
    print('Neither weak nor strong relationship')
