'''
Program: cities.py
Author: David Wells


'''
print("Using a break statement to Exit a Loop")
print("---------------------------------------")

prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
        
print("\n\n Thank you for playing along.\n")