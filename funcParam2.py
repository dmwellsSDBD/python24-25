'''
This program will accept 2 inputs from the user and process the data as exponents of one another.
'''

# This function prints the 2 user inputs and then calculates them as exponents of one another and prints them out to the terminal window
def myFunction(a, b):
    print("\nVariable a is: ", a, ".")
    print("\nVariable b is: ", b, ".")
    exp1 = a ** b
    exp2 = b ** a
    print("\n", a, " to the power of ", b, "is: ", exp1)
    print("\n", b, " to the power of ", a, "is: ", exp2)
    
def sum(first, second):
    total = first + second
    print("The total of your data input is:", total)
    

# Ask the user for 2 integers between 1 and 10
a = int(input("\nPlease enter a number between 1 and 10: "))
b = int(input("\nPlease enter a number between 1 and 10: "))

myFunction(a, b)


print("\nPart 2 of our Example:\n")

# Give the user the option to repeat this process as many times as they want.
# If they want to quit, they type the word 'Quit'
while True:

    # Have users input positive integers
    myVar1 = int(input("Please Enter an positive whole number: "))
    myVar2 = int(input("Please Enter an positive whole number: "))

    # call the sum() function to process the user input
    sum(myVar1, myVar2)
    
    
    # Explain to the user how to quit this process
    print("\nIf you would like quit this application select one of these options:")
    print("1. Quit")
    print("2. Continue")
    menu = input("\nPick 1 or 2: ")
    
    if menu == '1':
        break
    else:
        print("\nHere we go again...\n")

print("\nWe are sorry to see you go! Have a great day!!\n\n")