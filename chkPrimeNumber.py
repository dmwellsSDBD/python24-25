def  is_prime(number):
    """
    Check if a number is a prime number.

    Args:
        number (int): The number to check from the user
        
    Return:
        bool: True if the number is prime, False if it isn't
    """
    
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        
    return True # It is a Prime Number

# Example usage
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")