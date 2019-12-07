"""Program to find the probability that a woman has cancer if she has a positive mammogram result
1. 1% of women over 50 have breast cancer
2. 90% of women who have breast cancer test positive on mammograms
3. 8% of women will have false positives
"""
p_cancer = 0.01
p_cancer_positive = 0.90      # probability +ve test and cancer victim
p_noCancer_positive = 0.08     # probability + ve test and no cancer victim
# finding probability of all +ve tests i.e irrespective of cancer or not
total_positive = p_cancer*p_cancer_positive + (1-p_cancer)*p_noCancer_positive
# out of all positive tests finding cancer victims i.e. cancer given +ve test
print(f'P (cancer given +ve test): {round(p_cancer*p_cancer_positive/total_positive,4)*100} %')



