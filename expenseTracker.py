"""
Title: Expense Tracker with Category Summaries

Description: This program allows users to add expenses with categories, view the total expenses, and see a summary of expenses by category. It uses functions with multiple steps, internal calculations, and return values.

Choose an Option:

Application Menu:
    1. Add Expense
    2. View Total Expenses
    3. View Expense Report - Broken into 2 functions (1. Get Summary, 2. Display Summary)
    4. Quit
    
4 Primary Processes (Functions) based on the options from the menu.

Data Structure: 
    Python Dictionary 
    
    myDictionary = {
        key1 : value1,
        key2 : value2,
        ...
        keyn : valuen
    }
"""

# Define the functions for our application

def add_expenses(expenses, category, amount):
    """
    Add an expense to the tracker.
    
    Args:
        expenses (dict): A dictionary where keys are categories and values are lists of expense amounts
        category (str): The category of the expense
        amount (float): The amount of the expense.
        
    Returns:
        dict: The update dictionary of expenses.
    """
    
    if category not in expenses:
        expenses[category] = []
    
    expenses[category].append(amount)
    
    return expenses
    
def get_total_expenses(expenses):
    """
    Calculate the total expenses across all categories.
    
    Args:
        expenses (dict): A dictionary where kesy are categories and values are lists of expense amounts
        
    Returns:
        float: The total amount of expenses
    """
    
    return sum(sum(amounts) for amounts in expenses.values())
    
    
def get_category_summary(expenses):
    """
    Provide a summary of expenses by category.
    
    Args:
        expenses (dict): A dicitonary where keys are categories and values are lists of expense amounts
        
    Returns:
        dict: Our ever expanding dictionary
    """
    
    return {category: sum(amounts) for category, amounts in expenses.items()}
    
def display_expense_report(expenses):
    """
    Display a detailed expense report.
    
    Args:
        expenses (dict): A dicitonary where keys are categories and values are lists of expense amounts
        
    Returns:
        NONE
    """
    
    print("\n--- Expense Report ---")
    category_summary = get_category_summary(expenses)
    total_expenses = get_total_expenses(expenses)
    
    
    

# Create and empty dictionary to hold all of our data
expenses = {}

print("\n\n")
print("###########################################")
print("###                                     ###")
print("###         MY EXPENSE TRACKER          ###")
print("###                                     ###")
print("###########################################")
print("\n")

while True:
    
    # Create the application menu
    print("\n########### MENU #############\n")
    print("1. Add Expense")
    print("2. View Total Expenses")
    print("3. View Expense Report") 
    print("4. Quit")
    
    # Ask the user what they want to do
    choice = input("Enter your choice: ")
    
    # User has 4 options, this section will control what happens with each option selected
    if choice == "1":
        category = input("Enter the expense category (e.g. Food, Transportation, Utilities, etc.)")
        amount = float(input("Enter the expense amount: "))
        expenses = add_expenses(expenses, category, amount)
        # expenses gets returned from the function, and assigned to an expenses variable
        # the variable expenses does not get used yet
        
        print("Expense added successfully!")
        
    elif choice == "2":
        total = get_total_expenses(expenses)
        print(f"Total expenses so far: ${total:.2f}")
        
    elif choice == "3":
        display_expense_report(expenses)
        
    # End the application and avoid an Infinite Loop
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose again: ")