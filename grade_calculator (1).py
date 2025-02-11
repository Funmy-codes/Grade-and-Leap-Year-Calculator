# -*- coding: utf-8 -*-
"""Grade Calculator


#### A Grade Calculator
"""

# Print a welcome message to the user
print('Welcome to my Grade Calculator')

# Get the user's grade as input and convert it to an integer
grade = int(input('Enter your grade: '))

# Check if the grade is between 0 and 40 (inclusive)
if grade > 0 and grade <= 40:
    # If true, print that the grade corresponds to an F
    print(f"You scored {grade} so that's a F")

# Check if the grade is between 41 and 50 (inclusive)
elif grade > 40 and grade <= 50:
    # If true, print that the grade corresponds to a P (Pass)
    print(f"You scored {grade} so that's a P")

# Check if the grade is between 51 and 70 (inclusive)
elif grade > 50 and grade <= 70:
    # If true, print that the grade corresponds to a C (Credit)
    print(f"You scored {grade} so that's a C")

# Check if the grade is between 71 and 100 (inclusive)
elif grade > 70 and grade <= 100:
    # If true, print that the grade corresponds to an A
    print(f"You scored {grade} so that's an A")

# If none of the above conditions are true (grade is outside 0-100), print an error message
else:
    print('Input a number less than 100 and greater than 0')
