# Multiplication Module
# This module provides multiplication functionality for the calculator

def mul(a, b):
    """
    Multiply two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    """
    return a * b

# Test the function if run directly
if __name__ == "__main__":
    print("Testing mul function:")
    print(f"mul(10, 5) = {mul(10, 5)}")
    print(f"mul(100, 250) = {mul(100, 250)}")
    print(f"mul(-5, 15) = {mul(-5, 15)}")
