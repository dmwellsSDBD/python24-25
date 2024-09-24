'''
Author: David Wells
Program: forSummationEx.py

Collect lower bound
Collect upper bound
Perform a Summation process using those limits in a for loop
'''

lower = int(input("Enter the lower bound: "))# int() converts data to an integer
upper = int(input("Enter the upper bound: "))

theSum = 0

for number in range(lower, upper):
    theSum = theSum + number

print("The summation of ", lower , " to ", upper, " is: ", theSum)