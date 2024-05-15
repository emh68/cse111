
print("""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
)

# Get user's age and convert to integer
age = int(input("Please enter your age: "))

# Calculate heart rate min and max
heart_rate_min = int((220 - age) * .65)
heart_rate_max = int((220 - age) * .85)

# Print result message
print(f"When you exercise to strengthen your heart, you should keep your heart rate "
      f"between {heart_rate_min} and {heart_rate_max} beats per minute. ")
