def is_power_of_two(num):
    """
    Function to check if a number is a power of two.
    
    Args:
        num (int): The number to be checked.
    
    Returns:
        bool: True if num is a power of two, False otherwise.
    """
    # Check if num is greater than 0 and if it has only one bit set to 1
    return num > 0 and (num & (num - 1)) == 0

# Taking input from the user
num = int(input("Enter an integer: "))

# Checking if the input number is a power of two
result = is_power_of_two(num)

# Printing the result
print(f"{num} is a power of two: {result}")
