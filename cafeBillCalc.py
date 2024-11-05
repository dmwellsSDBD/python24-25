# Constants
SERVICE_TAX = 0.1  # 10% service tax

# Function to calculate the total bill
def calculate_total(coffee_price, pastry_price, juice_price):
    subtotal = coffee_price + pastry_price + juice_price
    total = subtotal + (subtotal * SERVICE_TAX)
    return total

# User inputs
coffee_price = float(input("Enter the price of coffee: $"))
pastry_price = float(input("Enter the price of pastry: $"))
juice_price = float(input("Enter the price of juice: $"))

# Calculate total bill
total_bill = calculate_total(coffee_price, pastry_price, juice_price)

# Print total bill
print("Your total bill, including service tax, is: $", round(total_bill, 2))