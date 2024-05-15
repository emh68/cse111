from datetime import datetime

current_date_time = datetime.now()
day_of_week = current_date_time.weekday()
day_of_week = 4
price = 1
discount = 0
subtotal = 0

#subtotal = float(input('Please enter the subtotal: '))
while price != 0:
    price = float(input('What is the price of the product? '))
    if price != 0:
        quantity = int(input('How many of that item did you buy? '))
        subsubtotal = price * quantity
        subtotal += subsubtotal


if subtotal >= 50 and(day_of_week == 1 or day_of_week == 2):
    discount = subtotal * .10
    print(f'Discount amount: {discount:.2f}')

if subtotal < 50 and(day_of_week == 1 or day_of_week == 2):
    print(f'You only need to spend ${50-subtotal:.2f}')


tax = (subtotal-discount) * .06

print(f'Sales tax amount: {tax:.2f}')
print(f'Total: {(subtotal-discount)+tax:.2f}')