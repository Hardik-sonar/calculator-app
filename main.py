# Version 1.0 - Initial Release
# Calculator Application - Main File
# This file integrates all calculator operations

# Import functions from feature modules
from add import add
from sub import sub
from mul import mul

def main():
    """Main function to demonstrate calculator operations"""
    print("Calculator Application")
    print("=" * 40)
    
    # Test values
    num1 = 10
    num2 = 5
    
    # Call add function
    result_add = add(num1, num2)
    print(f"Addition: {num1} + {num2} = {result_add}")
    
    # Call sub function
    result_sub = sub(num1, num2)
    print(f"Subtraction: {num1} - {num2} = {result_sub}")
    
    # Call mul function
    result_mul = mul(num1, num2)
    print(f"Multiplication: {num1} * {num2} = {result_mul}")
    
    print("\n" + "=" * 40)
    print("All features successfully integrated!")

if __name__ == "__main__":
    main()
