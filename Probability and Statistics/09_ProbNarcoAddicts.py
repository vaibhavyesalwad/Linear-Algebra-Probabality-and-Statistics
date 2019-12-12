""" In a particular pain clinic, 10% of patients are prescribed narcotic pain killers.
Overall, 5 % of the clinic’s patients are addicted to narcotics (including pain killers and illegal substances).
Out of all the people prescribed pain pills, 8% are addicts. If a patient is an addict
Write a program to find the  probability that they will be prescribed pain pills"""
from fractions import Fraction
p_prescription = Fraction(1, 10)                  # p_noPrescription = 1- p_prescription
# probability of addicts is from total patients
p_addict = Fraction(1, 20)
# p_addict = p_prescription*p_prescription_addict + (1-p_prescription)*p_noPrescription_addict
p_prescription_addict = Fraction(2, 25)   # given
p_noPrescription_addict = 1 - p_prescription*p_prescription_addict  # calculated
print(f'P (prescribed pain killer / addict): {round(p_prescription*p_prescription_addict/p_addict, 4)*100} %')


