"""
Assume that two variables, varA and varB, are assigned values, either numbers or strings.

Write a piece of Python code that prints out one of the following messages:

"string involved" if either varA or varB are strings

"bigger" if varA is larger than varB

"equal" if varA is equal to varB

"smaller" if varA is smaller than varB

"""

if type(varA) is str or type(varB) is str:
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
else:
    print("smaller")
