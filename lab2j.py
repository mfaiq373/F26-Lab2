# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use while loops with break and continue.
# Usage: ./lab2j.py

# TO DO 1: 
# Import the `math` module.
# Define a variable named num. Prompt the user to input a number and assign it to the variable num.
# Convert the user input to a floating-point number and assign it to num.
import math
num = float(input("enter a number: "))
while True:
    num = float(input("enter a number: "))
    if num < 0:
        print("invalid num")
        continue
    if num==0:
        print("Exiting...")
        break
    print(math.sqrt(num))
# TO DO 1: Import the `math` module.
    

# TO DO 2: Create an infinite loop using while True.

    # TO DO 3: Check if num is zero:
   

    # TO DO 4: Calculate the square root of num using the math.sqrt function.

