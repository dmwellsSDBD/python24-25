import math

area = float(input("Enter the area: "))

if area > 0:
    radius = math.sqrt(area / math.pi)
    print("The radius is", radius)
else:
    print("Error: the area must be a positive number.")
    area = float(input("Enter the area: "))
    radius = math.sqrt(area / math.pi)
    print("The radius is", radius)
    
print("\n\nExample 2: Maximum and minimum numbers")
print("--------------\n")

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first > second:
    maximum = first
    minimum = second
else:
    maximum = second
    minimum = first

print("Maximum number is: ", maximum)
print("Minimum number is: ", minimum)
