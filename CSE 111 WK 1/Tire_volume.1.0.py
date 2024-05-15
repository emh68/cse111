# Import math to use pi
import math

# Get inputs from user for width, aspect ratio and diameter
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate volume of tire
volume = math.pi * width ** 2 * aspect_ratio * \
    (width * aspect_ratio + 2_540 * diameter) / 10_000_000_000

# Print results
print("")
print(f"The approximate volume is {volume: .02f} liters")
