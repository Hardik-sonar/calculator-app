# Subtraction Module
# This module provides subtraction functionality for the calculator

def sub(a, b):
    """
    Subtract b from a and return the result.
    
    Args:
        a: First number (minuend)
        b: Second number (subtrahend)
    
    Returns:
        Difference of a and b (a - b)
    """
    return a - b

# Test the function if run directly
if __name__ == "__main__":
    print("Testing sub function:")
    print(f"sub(10, 5) = {sub(10, 5)}")
    print(f"sub(100, 250) = {sub(100, 250)}")
    print(f"sub(-5, 15) = {sub(-5, 15)}")
