import math

area = float(input("Enter the area of your circle: "))

if area > 0:
    radius = math.sqrt(area / math.pi)
    print("The radius of your circle is: ", radius)
else:
    print("Error: the area must be a positive number")
    area = float(input("Enter the area of your circle: "))
    
print("\n\nPart 2 of the Application: \n\n")

first = int(input("Enter your first positive number: "))
second = int(input("Enter your second positive number: "))

# More code goes here
if first > second:
    highest = first
    lowest = second
else:
    highest = second
    lowest = first

# Final state of the program
print("The HIGHEST number is: ", highest)
print("The LOWEST number is: ", lowest)
    
print("\n\nPart 3 of the Application: \n\n")

print("Logical Operators and Compound Boolean Expressions")
print("___________________________________________________\n\n")

number = int(input("Enter the students numeric grade: "))
# if number > 100:
#     print("Error: grade must be between 100 and 0")
# elif number < 0:

if number > 100 or number < 0:   ### Compound Conditional  
    # if number < 0 or number > 100
    print("Error: grade must be between 100 and 0")
else:
    # Code to convert numeric grade to Letter grade goes here
    # Create a function: letterGrade()
    # Converts number to A, B, C, D, F
    # A >= 90, B >= 80, C >= 70, D >= 60, F < 60
    if number >= 90:
        print("Your letter grade is an A")
    elif number >= 80 and number <= 89:
        print("Your letter grade is a B")
    elif  number >= 70 and number <= 79:
        print("Your letter grade is a C")
    elif number >= 60 and number <= 69:
        print("Your letter grade is a D")
    else:
        print("You got an F you FAILURE!!")