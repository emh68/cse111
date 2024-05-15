"""The code includes added functionality that exceeds requirements. 
If the current day is Tuesday or Wednesday all products are discounted 10%.
The following code imports a csv of the products a store has and a csv of items 
and the quantity of items that a customer is requesting to order. The program 
then calculates the subtotal, tax and total amount the customer owes. 
If the day is Tuesday or Wednesday, the program discounts all of the products by 10%."""

from datetime import datetime
import csv


def main():
    PRODUCT_NUMBER_INDEX = 0
    QUANTITY_INDEX = 1
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
    STORE_NAME = "Hansen's Market"

    # Get the current day of the week.
    current_day = datetime.now().weekday()

    # Read products csv and convert to dictionary called products_dict.
    products_dict = read_dictionary("products.csv", PRODUCT_NUMBER_INDEX)

    # print store name.
    print(STORE_NAME)
    print()

    # Initialize a num_items and subtotal variable,
    # so that values can be added to each of these variables.
    num_items = 0
    subtotal = 0

    # File Not Found and PermissionError exceptions.
    try:

        # Open a file named request.csv and store a reference
        # to the opened file in a variable named request_file.
        with open("request.csv", "rt") as request_file:

            # Use the csv module to create a reader
            # object that will read from the opened file.
            reader = csv.reader(request_file)

            # The first row of the CSV file contains column
            # headings and not data, so this statement skips
            # the first row of the CSV file.
            next(reader)

            # Read each row in the CSV file one at a time.
            # The reader object returns each row as a list.
            for row_list in reader:

                # For the current row, retrieve the
                # values in columns 0 and 1.
                product_number = row_list[PRODUCT_NUMBER_INDEX]
                product_quantity = int(row_list[QUANTITY_INDEX])

                # KeyError exception.
                try:
                    # Check if the product number is in the products dictionary.
                    # if product_number in products_dict:

                    # Find the product number in the dictionary and
                    # retrieve the corresponding value, which is a list.
                    value = products_dict[product_number]

                    # Retrieve the product name and product price from the list.
                    product_name = value[PRODUCT_NAME_INDEX]
                    product_price = float(value[PRODUCT_PRICE_INDEX])

                    # Calculates a 10% discount on products if
                    # the current day is Tuesday or Wednesday.
                    if current_day == 1 or current_day == 2:
                        product_price *= .90

                    # Print product name, quantity and price.
                    print(
                        f"{product_name}: {product_quantity} @ {product_price:.02f}")

                    # Calculate the number of items customer requests,
                    # the subtotal, sales tax and total price.
                    num_items += product_quantity
                    subtotal += product_quantity * product_price
                    sales_tax = subtotal * .06
                    total = subtotal + sales_tax

                except KeyError as key_err:
                    print(f"Product with number {product_number} not found.")
                    print(type(key_err).__name__, key_err)

    except FileNotFoundError as not_found_err:
        print(not_found_err)

    except PermissionError as perm_err:
        print(perm_err)

    # Print number of items, subtotal, sales tax and total.
    print()
    print(f"Number of Items: {num_items}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")

    # Prints thank you for shopping and the store name.
    print()
    print(f"Thank you for shopping at the {STORE_NAME}!")

    # Prints the current day and time.
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%a %b %d %Y, %I:%M %p}")


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

    # Return the dictionary
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()
