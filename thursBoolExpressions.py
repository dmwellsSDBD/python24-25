print("Example 1:\n\n")

# Program will check if a number is even or odd
number = 7

# number = int(input("Input any whole number: "))

if number % 2 == 0:
    print(number , "is Even.")
else:
    print(number , "is Odd.")
    
    
print("\n\nExample 2: \n\n\n")

# Program will check if a person is eligible to vote
age = 22

if age >= 18:
    print("Yes they can vote.")
else:
    print("No they cannot vote.")
    
print("\n\nExample 3:\n")

# Program to check if login credentials are correct
username = input("Enter your username: ")  # "admin"
password = input("Enter your password: ")  #"password123"

if username == "admin" and password == "password123":
    print("Login Successful: Please Proceed with Grading.")
else:
    print("You are not authorized to use this system")
    
print("\n\nExample 4: \n")

grade = int(input("Please enter Eva's grade for the test: "))

if grade >= 90:
    print("Eva got an A on the Test")
elif grade >= 80:
    print("Eva got an B on the Test")
elif grade >= 70:
    print("Eva got an C on the Test")
elif grade >= 60:
    print("Eva got an D on the Test")
else:
    print("Eva got an F on the Test")