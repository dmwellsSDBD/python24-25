'''
Booleans - represent 2 possible values: True or False (1 or 0 in Binary)
'''

print("\n\nExample of using Boolean values: \n")

isRaining = False
isSunny = True

print(isRaining) # Output: False
print(isSunny) # Output: True
print()

'''
Logical Operators:
and - Returns True if both statements are True
or - Returns True if one of the statements is True
not - Reverses the Boolean value
'''

print("\nLogical Operators Examples:\n")

# 2 variables
isWeekend = False
isHoliday = False

# Using "and"
print(isWeekend and isHoliday) # Output - False

# Using "or"
print(isWeekend or isHoliday) # Output - False

# Using "not"
print(not isWeekend) # Output - True

print(not isHoliday and isWeekend) # Output - False

print(not isHoliday and not isWeekend) # Output - True

print(not isWeekend or isHoliday) # Output - True

print()

'''
Comparison Operators
==  Equal To
!=  Not Equal to
>  Greater Than
<  Less Than
>=  Greater Than or Equal To
<=  Less Than or Equal To
'''

print("\nExample of Comparison Operators\n")

x = 10
y = 20

print(x == y) # Output False
print(x != y) # Output True
print(x < y) # Output True
print(x >= y) # Output False

if x < y:
    #code
    print("This is the if code")
else:
    #else code
    print("This is the else code")
    
print()

'''
if Statement: lets the program decide what code to run based on a condition
'''

print("\nExample of an if Statement")

num1 = 5
num2 = 2

if num2 > num1:
    print("first if code block")
else:
    print("first else code block")
    
if num1 ** num2 > 20:
    print("second if code block")
else:
    print("second else code block")
    
if num1 ** num2 != 25:
    print("third if code block")
else:
    print("third else code block")
    
print()

'''
for Loop - used to iterate over a sequence(exp. a list or range of items)
Iteration - every time you repeat something is an iteration
'''
print("\n in range for Loop Example:\n")
for i in range(5):
    print("Iteration:", i) # Output 
    
print("\nList Iteration for Loop Example\n")

myList = ["Gavin", "Hunter", "Hannah", "Connor", "Eva", "Christian"]

for i in myList:
    print(i)
    print(len(myList))


'''
while Loops - a Loop that continues running as long as its condition is True
BE CAREFUL of Infinite Loops
'''

print("\nExample of a while Loop\n")

counter = 3

while counter > 0:
    print("Countdown:", counter)
    counter -= 1

print("Blast off!")

print("\nExample 2 of a while Loop\n")

x = 5
y = 6
z = 5 * 6 # 30

while True:
    
    if z > 90:
        break
    else:
        print(z)
        x = 10
        y = 12
        z = x * y

print(z)
print()
