
from datetime import datetime


subtotal = float(input("Please enter your subtotal: $"))

current_date_and_time = datetime.now(tz=None)
day_of_week = datetime.weekday(current_date_and_time)

# day_of_week = 1

if subtotal >= 50 and day_of_week == 1 or day_of_week == 2:
    discount_amount = float(subtotal * .10)
    subtotal = subtotal - discount_amount
    sales_tax = float(subtotal * .06)
    total = subtotal + sales_tax

    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Sale tax amount: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")

else:
    sales_tax = float(subtotal * .06)
    total = subtotal + sales_tax

    print(f"Sale tax amount: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")



