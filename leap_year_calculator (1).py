# -*- coding: utf-8 -*-
"""Leap Year Calculator



### A leap Year Calculator
"""

# Print a welcome message to the user
print('Welcome to my leap year calculator')

# Get the year as input from the user and convert it to an integer
year = int(input('Enter a year: '))

# Check if the year is divisible by 400
if year % 400 == 0:
    # If true, it is a leap year
    print(f'{year} is a leap year')

# Check if the year is divisible by 100 (but not 400)
elif year % 100 == 0:
    # If true, it is not a leap year
    print(f'{year} is not a leap year')

# Check if the year is divisible by 4 (but not 100 or 400)
elif year % 4 == 0:
    # If true, it is a leap year
    print(f'{year} is a leap year')

# If none of the above conditions are true, it is not a leap year
else:
    print(f'{year} is not a leap year')
