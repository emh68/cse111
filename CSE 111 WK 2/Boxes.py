
"""
A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. Write a Python
program named boxes.py that asks the user for two integers:  1) the
number of manufactured items and 2) the number of items that the user
will pack per box. Your program must compute and print the number of
boxes necessary to hold the items. This must be a whole number. Note
that the last box may be packed with fewer items than the other boxes.
"""

# Import the math module
import math

# Get user input, two numbers
# How many items and how many items per box
num_of_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

# Calculate how many boxes needed by dividing # of items by # of items per box
num_boxes = num_of_items / items_per_box

# Print blank line
print()

# Print results using math.ceil function
# Can't have half a box so this function determines results to closest whole number
print(f"For {num_of_items} items, packing {items_per_box} items in each box, "
      f"you will need {math.ceil(num_boxes)} boxes.")
