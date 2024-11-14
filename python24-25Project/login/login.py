# Enhanced login system with registration and file-based credential storage

# Filename for storing user credentials
credentials_file = "user_data.txt"

def load_credentials():
    """Load credentials from file into a dictionary."""
    credentials = {}
    try:
        with open(credentials_file, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                credentials[username] = password
    except FileNotFoundError:
        pass  # File will be created during the first registration
    return credentials

def save_credentials(username, password):
    """Save new credentials to the file."""
    with open(credentials_file, "a") as file:
        file.write(f"{username},{password}\n")

def register():
    """Register a new user with a username and password."""
    print("\n--- User Registration ---")
    username = input("Create a username: ")
    password = input("Create a password: ")

    # Load current credentials to check if username already exists
    credentials = load_credentials()
    
    if username in credentials:
        print("Username already exists. Please choose a different username.")
    else:
        save_credentials(username, password)
        print("Registration successful! You can now log in.")

def login():
    """Login an existing user by verifying credentials from file."""
    print("\n--- User Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Load credentials from file
    credentials = load_credentials()

    if username in credentials and credentials[username] == password:
        print("Login successful! Welcome, " + username + ".")
    else:
        print("Login failed. Please check your username and password and try again.")

def main():
    """Main menu loop."""
    while True:
        print("\n--- Main Menu ---")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the main function
if __name__ == "__main__":
    main()