'''
Program: whileLoops.py
Author: David Wells
'''

theSum = 0.0
data = input("Enter a number or just enter to quit: ")

while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or just enter to quit: ")
    
print("The sum of your numbers is:", theSum)

print("\n\n\nComparing for Loop to while Loop")
print("-----------------------------------\n")

# Summation with for Loop
theSum = 0
for count in range(1, 100001):
    theSum += count
print(theSum)

# Summation with while Loops
theSum = 0 
count = 1
while count <= 100000:
    theSum += count
    count += 1

print("Our while Loop version: ", theSum)
