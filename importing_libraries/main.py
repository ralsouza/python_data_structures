# Importing libraries
import my_math
from my_math import area_square as arsq

def print_hi(name):
    print(f"Hi, {name}")

def fat(n):
    return my_math.fat(5)

def pow(base,pow):
    return my_math.pot(base,pow)

# Main function
if __name__ == "__main__":
    
    # Import my own libraries
    print_hi("My Name")
    print(f"Fatorial is: {fat(5)}")
    print(f"The power is: {my_math.pot(2,10)}")
    print(f"My area of square is: {arsq(100)}")

    