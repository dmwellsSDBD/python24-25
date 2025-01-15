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

def add_expenses():
    add = 1 + 1 # Remove this later
    
def get_total_expenses():
    add = 1 + 1 # Remove this later
    
def get_category_summary():
    add = 1 + 1 # Remove this later
    
def display_expense_report():
    add = 1 + 1 # Remove this later


while True:
    print("\n\n")
    print("###########################################")
    print("###                                     ###")
    print("###         MY EXPENSE TRACKER          ###")
    print("###                                     ###")
    print("###########################################")
    print("\n\n")
    
    
    # Create the application menu
    print("\n########### MENU #############\n")
    print("1. Add Expense")
    print("2. View Total Expenses")
    print("3. View Expense Report") 
    print("4. Quit")
    
    # Ask the user what they want to do
    choice = input("Enter your choice: ")
    
    # End the application and avoid an Infinite Loop
    if choice == "4":
        break