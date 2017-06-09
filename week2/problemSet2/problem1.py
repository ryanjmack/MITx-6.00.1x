"""
Created on Fri Jun  9 16:30:17 2017

@author: ryanjmack

Calculates the credit card balance after one year if a person only
pays the minimum monthly payment required by the credit card company
each month.
"""

# Test case 1's inputs
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for _ in range(12):
    minimum = balance * monthlyPaymentRate
    balance -= minimum
    balance *= (1 + annualInterestRate / 12)

print("Remaining balance: {}".format(round(balance, 2)))

#_____________________________________________________________________________
#         # Test Case 1:
#	      balance = 42
#	      annualInterestRate = 0.2
#	      monthlyPaymentRate = 0.04
#
#	      # Result Your Code Should Generate Below:
#	      Remaining balance: 31.38
#_____________________________________________________________________________
#         # Test Case 2:
#	      balance = 484
#	      annualInterestRate = 0.2
#	      monthlyPaymentRate = 0.04
#
#	      # Result Your Code Should Generate Below:
#	      Remaining balance: 361.61
