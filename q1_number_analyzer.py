import math

def number_analyzer():
    """Analyzes number properties"""

    # Input validation
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Enter a whole number.")
