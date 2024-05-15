""" This program gets user input, tire dimensions i.e. width, aspect ratio and diameter and calculates
tire volume. It then writes the dimension info. and date and time to a .txt file named volumes.
I have included additional functionality for the exceeds requirement, by asking the user if they would
like to buy tires with these dimensions, if user enters 'yes' they are prompted for their phone number.
If user answers 'no' the word 'none' is written to the .txt file indicating no phone number."""


# Import math to use pi
# Import datetime class from datetime
import math
from datetime import datetime

# Get inputs from user for width, aspect ratio and diameter
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate volume of tire
volume = math.pi * width ** 2 * aspect_ratio * \
    (width * aspect_ratio + 2_540 * diameter) / 10_000_000_000

# Print tire volume results
print("")
print(f"The approximate volume is {volume: .02f} liters\n")

# Ask if customer would like to buy tires with the given dimensions
buy_tires = input(
    "Would you like to buy tires with these dimensions? (yes or no) ").lower()

# If customer wants to buy tires prompt to get customer phone number
phone_num = ""
if buy_tires == "yes" or buy_tires == "y":
    phone_num = input("Please enter your phone number: ")
else:
    phone_num = "none"

# Get the current date and time of the week
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

# Create text file and store tire volume and dimensions. If customer wants to but tires get and store phone number
with open("volumes.txt", mode="at") as volume_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume: .02f}, {phone_num}",
          file=volume_file)
