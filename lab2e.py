# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

# TO DO 1: Follow the instructions given in README.md file
import sys
#print(sys.platform)
#print(sys.argv)
num_args=len(sys.argv)-1
if num_args<2:
    print("this script requires at least 2 arguments")
else:
    name=sys.argv[1]
    age=sys.argv[2]
    if num_args == 2:
        print(f"Hi {name} , you are {age} years old and the script recieved only 2 arguments")
    else:
        print(f"this script requires exactly 2 arguments. You provided three arguments")