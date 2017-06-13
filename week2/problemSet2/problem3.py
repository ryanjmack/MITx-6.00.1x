def calculate(lowerbound, upperbound):
"""
program the returns the smallest monthly payment such that
will pay off the an entire loan balance within a year,
taking into account the accrual of interest at different rates
depending on how much is paid each month
"""

    # need to preserve the state of balance (global) for further calculations
    owed = balance
    middle = (lowerbound + upperbound) / 2

    # iterate over the 12 months
    for _ in range(12):
        owed -= middle
        owed *= (monthlyInterestRate + 1)

    # bisection search - cuts potential results in half
    if owed > 0:
        calculate(middle, upperbound)
    # paid, but can we pay even less?
    elif owed < 0 and upperbound - lowerbound > 0.01:
        calculate(lowerbound, middle)
    else:
        print("Lowest payment: {}".format(round(middle, 2)))
        return

# balance & annualInterestRate are test case 1's inputs
balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12

# minimum we would have to pay (unless an interest free loan)
lowerbound = balance / 12
# max interest accrual if we didn't pay a single dime until the last month
upperbound = balance * (monthlyInterestRate + 1)**12 / 12

# call calculate
calculate(lowerbound, upperbound)


#
# TEST CASES
#__________________________________
# Test Case 1:
# balance = 320000
# annualInterestRate = 0.2
#
# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 29157.09
#
#__________________________________
# Test Case 2:
# balance = 999999
# annualInterestRate = 0.18
#
# Result Your Code Should Generate:
#-------------------
#Lowest Payment: 90325.03
#
