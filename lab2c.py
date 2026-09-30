
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Practice using if, elif, and else statments.
# Usage: ./lab2c.py

# TO DO 1:
# Prmopt the user to enter a sentence, save it in the variable str1
# Prmopt the user to enter another sentence, save it in the variable str2
str1 = input("please write someting: ")
str2 =input("please write something again!: ")
#
# Use if, elif, and else statments with the len() function to check which of the 2 is longer.
# The final result should be:
# ---- is longer then ----
if len(str1) != len(str2):
 if (len(str1) > len(str2)):
    print(f"{str1} is greater than {str2}")
 else:
    print(f"{str2} is greater than {str1}")
# If they are equal then print:
# ---- and ---- are equal.
if len(str1) == len(str2):
   print(f"{str1} and {str2} are equal")
# Get input from the user



