"""
Created on Fri Jun  9 16:45:30 2017

@author: ryanjmack

Program that calculates the minimum fixed monthly payment needed in order pay
off a credit card balance within 12 months. By a fixed monthly payment,
we mean a single number which does not change each month, but instead is
a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The monthly payment must be a multiple of $10 and is the same for all months.
Notice that it is possible for the balance to become negative using this
payment scheme, which is okay

"""
import math

# Test case 1's balance & interest rate
balance = 3926
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12

# this is the starting point for the calculations - we divide the balance
# by 12 months to get a monthly amount that will payoff the principal. As per
# spec in the docstring this number must be a multiple of 10. So we round up
# to the nearest tens place and cast to an int.
monthlyPayment = int((math.ceil(balance / 120) * 10))

# each iteration checks if the monthly payment can pay the balance, if not
# increase the monthly payment and check again
while True:
    # copy the value in balance
    amount = balance

    for _ in range(12):
        amount -= monthlyPayment
        amount *= (1 + monthlyInterestRate)

    if amount <= 0:
        break
    else:
        monthlyPayment += 10

print("Lowest payment: {}".format(monthlyPayment))


#TEST CASES:
#__________________________________________
#         # Test Case 1:
#	      balance = 3329
#	      annualInterestRate = 0.2
#
#	      Result Your Code Should Generate:
#	      -------------------
#	      Lowest Payment: 310
#         _________________________________
#
#	      # Test Case 2:
#	      balance = 4773
#	      annualInterestRate = 0.2
#
#	      Result Your Code Should Generate:
#	      -------------------
#	      Lowest Payment: 440
#
#         ________________________________
#	      # Test Case 3:
#	      balance = 3926
#	      annualInterestRate = 0.2
#
#	      Result Your Code Should Generate:
#	      -------------------
#	      Lowest Payment: 360
#
