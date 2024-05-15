# n = float(input("Please enter a number: "))
# r = round(n)
# print(r)


# x = "sun"
# y = "moon"
# z = "stars"
# print(x, y, z, sep="\n", flush=True)

# x = "sun"
# y = "moon"
# z = "stars"
# print(x, y, z, sep="|", flush=True)


# import math
# x = 71
# r = math.sqrt(x)
# print(r)


# import math
# x = 71
# r = round(math.sqrt(x))
# print(r)


# import math
# x = 71
# r = round(math.sqrt(x), 2)
# print(r)

# # Example 6

# # Get a string of text from the user.
# text1 = input("Enter a motivational quote: ")

# # Call the built-in len function to get
# # the number of characters in the text.
# length = len(text1)
# print(length)
# # Call the string upper method to convert
# # the quote to upper case characters.
# text2 = text1.upper()

# # Call the built-in print function to print
# # the length of the text and the text in all
# # upper case for the user to see.
# print(length, text2)


# # Example 7

# import math

# # Get a number from the user.
# number = float(input("Enter a number: "))

# # Call the math.sqrt function and
# # immediately print its return value.
# print( math.sqrt(number) )

# # Call the math.sqrt function again and
# # use its return value in an if statement.
# if math.sqrt(number) < 100:
#     print(f"The square root is less than 100.")
# elif math.sqrt(number) > 100:
#     print(f"The square root is more than 100.")
# else:
#     print(f"The square root is exactly 100.")


# # Example 8
# # It is better to store the math.sqrt(number) as a variable and reuse it rather than type the function
# # multiple times like in example 7. It is faster.
# import math

# # Get a number from the user.
# number = float(input("Enter a number: "))

# # Call the math.sqrt function and store its
# # return value in a variable to use later.
# root = math.sqrt(number)

# print(f"The square root is {root:.2f}")

# if root < 100:
#     print(f"The square root is less than 100.")
# elif root > 100:
#     print(f"The square root is more than 100.")
# else:
#     print(f"The square root is exactly 100.")


# # Import the datetime class from the datetime
# # module so that it can be used in this program.
# from datetime import datetime

# # Call the now() method to get the current
# # date and time as a datetime object from
# # the computer's operating system.
# current_date_and_time = datetime.now()

# # Call the weekday() method to get the day of the
# # week from the current_date_and_time object.
# day_of_week = current_date_and_time.weekday()

# # Print the day of the week for the user to see.
# print(day_of_week)

# import datetime

# def print_time():
#     print("task completed")
#     print(datetime.datetime.now())
#     print()

# first_name = "Susan"
# print_time()

# for x in range(0,10):
#     print(x)
# print_time()

# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial

# first_name = input("Enter your first name: ")
# first_name_initial = get_initial(first_name)

# last_name = input("Enter your last name: ")
# last_name_initial = get_initial(last_name)


# print("Your initials are: " + first_name_initial + last_name_initial)


# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# print("Your initials are: " + get_initial(first_name) + get_initial(last_name))


# from datetime import datetime

# # Print timestamps to see how long sections of code take to run

# # Function to print current date and time
# def print_time():
#     print("task completed")
#     print(datetime.now())
#     print()

# first_name = "Susan"
# print_time()

# for x in range(0,10):
#     print(x)
# print_time()


# from datetime import datetime

# # Print timestamps to see how long sections of code take to run

# # Function to print current date and time
# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())
#     print()

# first_name = "Susan"
# print_time("printed first name")

# for x in range(0,10):
#     print(x)
# print_time('completed for loop')


# def get_initial(name, force_uppercase):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial

# first_name = input("Enter your first name: ")
# first_name_initial = get_initial(first_name, False)

# print("Your initial is: " + first_name_initial)

# # Example 1

# import math

# # Define a function named print_cylinder_volume.
# def print_cylinder_volume():
#     """Compute and print the volume of a cylinder.
#     Parameters: none
#     Return: nothing
#     """
#     # Get the radius and height from the user.
#     radius = float(input("Enter the radius of a cylinder: "))
#     height = float(input("Enter the height of a cylinder: "))

#     # Compute the volume of the cylinder.
#     volume = math.pi * radius**2 * height

#     # Print the volume of the cylinder.
#     print(f"Volume: {volume:.2f}")

# print_cylinder_volume()


# # Example 2

# import math

# # Define a function named print_cylinder_volume.
# def print_cylinder_volume(radius, height):
#     """Compute and print the volume of a cylinder.
#     Parameters
#         radius: the radius of the cylinder
#         height: the height of the cylinder
#     Return: nothing
#     """
#     # Compute the volume of the cylinder.
#     volume = math.pi * radius**2 * height

#     # Print the volume of the cylinder.
#     print(volume)

# print_cylinder_volume(2.5, 4.1)


# # Example 3

# import math

# # Define a function named computer_cylinder_volume.
# def compute_cylinder_volume(radius, height):
#     """Compute and return the volume of a cylinder.
#     Parameters
#         radius: the radius of the cylinder
#         height: the height of the cylinder
#     Return: the volume of the cylinder
#     """
#     # Compute the volume of the cylinder.
#     volume = math.pi * radius**2 * height

#     # Return the volume of the cylinder so that the
#     # volume can be used somewhere else in the program.
#     return volume

# volume = compute_cylinder_volume(2.5, 4.1)


# # Example 5

# import math

# # Define a function named main.
# def main():
#     # Get the radius and height from the user.
#     radius = float(input("Enter the radius of a cylinder: "))
#     height = float(input("Enter the height of a cylinder: "))

#     # Compute the volume of the cylinder.
#     volume = math.pi * radius**2 * height

#     # Print the volume of the cylinder.
#     print(f"Volume: {volume:.2f}")

# # Start this program by
# # calling the main function.
# main()


# # Example 6

# import math

# # Define the main function.
# def main():
#     # Get a radius and a height from the user.
#     radius = float(input("Enter the radius of a cylinder: "))
#     height = float(input("Enter the height of a cylinder: "))

#     # Call the compute_cylinder_volume function and store
#     # its return value in a variable to use later.
#     volume = compute_cylinder_volume(radius, height)

#     # Print the volume of the cylinder.
#     print(f"Volume: {volume:.2f}")


# # Define a function that accepts two parameters.
# def compute_cylinder_volume(radius, height):
#     """Compute and print the volume of a cylinder.
#     Parameters
#         radius: the radius of the cylinder
#         height: the height of the cylinder
#     Return: the volume of the cylinder
#     """
#     # Compute the volume of the cylinder.
#     volume = math.pi * radius**2 * height

#     # Return the volume of the cylinder so that the
#     # volume can be used somewhere else in the program.
#     # The returned result will be available wherever
#     # this function was called.
#     return volume


# # # Start this program by
# # # calling the main function.
# # main()

# import random

# # Create a list of strings and assign
# # the list to a variable named words.
# words = ["boy", "girl", "cat", "dog", "bird", "house"]

# # Call the random.choice function which will choose
# # one string from the words list. Store the chosen
# # string in a variable named word.
# word = random.choice(words)
# print(word)


# # Example 4

# # The variables e and f can be any floating-
# # point numbers from any calculation.
# e = 7.135
# f = 7.128

# if abs(e - f) < 0.01:
#     print(f"{e} and {f} are close enough so")
#     print("we'll consider them to be equal.")
# else:
#     print(f"{e} and {f} are not close and")
#     print("therefore not equal.")

# # Example 5

# def test_sqrt():
#     assert math.sqrt(5) == approx(2.24, rel=0.01)

# def deposit(amount):
#     # In order for this program to work correctly and
#     # for the bank records to be correct, we must not
#     # allow someone to deposit a zero or negative amount.
#     assert amount > 0

# deposit(0)

# def test_min():
#     assert min(7, -3, 0, 2) == -3

# # test_min()
#
# import math
#
# sqrt = math.sqrt(5)
# print(sqrt)
#


# def prefix(string1, string2):
#     """Return the prefix, if any, that appears in both string1 and
#     string2. In other words, return a string of the characters
#     that appear at the beginning of both string1 and string2. For
#     example, if string1 is "inconceivable" and string2 is
#     "inconvenient", this function will return "incon".

#     Parameters
#         string1: a string of text
#         string2: another string of text
#     Return: a string
#     """
#     # Convert both strings to lower case.
#     string1 = string1.lower()
#     string2 = string2.lower()

#     # Start at the beginning of both strings.
#     i = 0

#     # Repeat until the computer finds two
#     # characters that are not the same.
#     limit = min(len(string1), len(string2))
#     while i < limit:
#         if string1[i] != string2[i]:
#            break
#         i += 1

#     # Extract a substring from string1 and return it.
#     pre = string1[0 : i]
#     return pre


# def suffix(string1, string2):
#     """Return the suffix, if any, that appears in both string1 and
#     string2. In other words, return a string of the characters
#     that appear at the end of both string1 and string2. For
#     example, if string1 is "hilarious" and string2 is "nefarious",
#     this function will return "arious".

#     Parameters
#         string1: a string of text
#         string2: another string of text
#     Return: a string
#     """
#     # Convert both strings to lower case.
#     string1 = string1.lower()
#     string2 = string2.lower()

#     # Start at the end of both strings.
#     i1 = len(string1) - 1
#     i2 = len(string2) - 1

#     # Repeat until the computer finds two
#     # characters that are not the same.
#     limit = min(len(string1), len(string2))
#     for _ in range(limit):
#         if string1[i1] != string2[i2]:
#             break
#         i1 -= 1
#         i2 -= 1

#     # Extract a substring from string1 and return it.
#     suf = string1[i1+1 : ]
#     return suf

# # WEEK 6 
# # Example 2

# def main():
#     print("This program computes and prints the remaining")
#     print("balance for a loan with a fixed annual percentage")
#     print("rate and a fixed number of payments per year.")
#     print()
#     print("Please enter the following five values.")

#     principal = float(input("Principal amount: "))
#     annual_rate = float(input("Annual percentage rate: "))
#     years = int(input("Number of years in the life of the loan: "))
#     payments_per_year = int(input("Number of payments per year: "))
#     number_paid = int(input("Number of payments already paid: "))

#     balance = compute_balance(principal, annual_rate, years,
#             payments_per_year, number_paid)

#     print()
#     print(f"Balance remaining: {balance}")


# def compute_balance(princ, ar, years, ppy, ptd):
#     """Compute and return the balance remaining for a loan."""
#     payment = compute_payment(princ, ar, years, ppy)

#     print()
#     print(f"compute_balance({princ}, {ar}, {years}, {ppy}, {ptd})")

#     rate = ar / ppy
#     power = (1 + rate) ** ptd
#     print(f"    payment: {payment}  rate: {rate}  power: {power}")

#     balance = princ * power - payment * (power - 1) / rate
#     print(f"    balance: {balance:.2f}")

#     return round(balance, 2)


# def compute_payment(princ, ar, years, ppy):
#     """Compute and return the payment per period for a loan."""
#     print()
#     print(f"compute_payment({princ}, {ar}, {years}, {ppy})")

#     rate = ar / ppy
#     n = years * ppy
#     print(f"    rate: {rate}  n: {n}")

#     payment = princ * rate / (1 - (1 + rate) ** -n)
#     print(f"    payment: {payment:.2f}")

#     return round(payment, 2)


# # Start this program by
# # calling the main function.
# if __name__ == "__main__":
#     main()


# # Week 7 Practice

# # Lists
# names = ["Susan", "Christopher"]
# print(len(names))
# names.insert(0, "Bill")
# print(names)
# names.sort()
# print(names)

# names = ["Susan", "Christopher", "Bill", "Justin"]
# presenters = names[1:3]
# print(presenters)


# # Dictionaries
# person = {"first" : "Christopher"}
# person["last"] = "Harrison" # adds the key, value pair to the dictionary at the end
# print(person)           # prints the dictionary
# print(person["first"])  # prints the value linked to the key we call. In this case we call "first" and the value associated with that is "Christopher"


# # For loops 

# # Loops through the list and gives the items in the list as output
# for name in ["Christopher", "Susan"]:
#     print(name)

# # Looping through a list a number of times
# for index in range(0, 2):       # 0 represents the starting number of the range and 2 reperesents how many items to get
#     print(index)


# # Looping with a condition

# names = ["Christopher", "Susan"]
# index = 0
# while index < len(names):
#     print(names[index])
#     # Change the fondition!!
#     index = index + 1

# # Week 7
# # Example 1

# def main():
#     # Create a list that contains five strings.
#     colors = ["yellow", "red", "green", "yellow", "blue"]

#     # Call the built-in len function
#     # and print the length of the list.
#     length = len(colors)
#     print(f"Number of elements: {length}")

#     # Print the element that is stored
#     # at index 2 in the colors list.
#     print(colors[2])

#     # Change the element that is stored at
#     # index 3 from "yellow" to "purple".
#     colors[3] = "purple"

#     # Print the entire colors list.
#     print(colors)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# # Example 2

# def main():
#     # Create an empty list that will hold fabric names.
#     fabrics = []

#     # Add three elements at the end of the fabrics list.
#     fabrics.append("velvet")
#     fabrics.append("denim")
#     fabrics.append("gingham")

#     # Insert an element at the beginning of the fabrics list.
#     fabrics.insert(0, "chiffon")
#     print(fabrics)

#     # Determine if gingham is in the fabrics list.
#     if "gingham" in fabrics:
#         print("gingham is in the list.")
#     else:
#         print("gingham is NOT in the list.")

#     # Get the index where velvet is stored in the fabrics list.
#     i = fabrics.index("velvet")

#     # Replace velvet with taffeta.
#     fabrics[i] = "taffeta"

#     # Remove the last element from the fabrics list.
#     fabrics.pop()

#     # Remove denim from the fabrics list.
#     fabrics.remove("denim")

#     # Get the length of the fabrics list and print it.
#     n = len(fabrics)
#     print(f"The fabrics list contains {n} elements.")
#     print(fabrics)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# # Example 3

# def main():
#     # Create a list of color names.
#     colors = ["red", "orange", "yellow", "green", "blue"]

#     # Use a for loop to print each element in the list.
#     for color in colors:
#         print(color)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# # Example 4

# def main():
#     # Count from zero to nine by one.
#     for i in range(10):
#         print(i)
#     print()

#     # Count from five to nine by one.
#     for i in range(5, 10):
#         print(i)
#     print()

#     # Count from zero to eight by two.
#     for i in range(0, 10, 2):
#         print(i)
#     print()

#     # Count from 100 down to 70 by three.
#     for i in range(100, 69, -3):
#         print(i)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# # Example 5

# def main():
#     # Create a list of color names.
#     colors = ["red", "orange", "yellow", "green", "blue"]

#     # Use a for loop to print each element in the list.
#     for color in colors:
#         print(color)

#     print()

#     # Use a different for loop to
#     # print each element in the list.
#     for i in range(len(colors)):
#         # Use the index i to retrieve
#         # an element from the list.
#         color = colors[i]

#         print(color)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# # Example 6

# def main():
#     sum = 0

#     # Get ten or fewer numbers from the user and
#     # add them together.
#     for i in range(10):
#         number = float(input("Please enter a number: "))
#         if number == 0:
#             break
#         sum += number

#     # Print the sum of the numbers for the user to see.
#     print(f"sum: {sum}")


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# # Example 7

# def main():
#     list1 = ["red", "orange", "yellow", "green", "blue"]
#     list2 = ["red", "orange", "green", "green", "blue"]

#     index = compare_lists(list1, list2)
#     if index == -1:
#         print("The contents of list1 and list2 are equal")
#     else:
#         print(f"list1 and list2 differ at index {index}")


# def compare_lists(list1, list2):
#     """Compare the contents of two lists. If the contents
#     of the two lists are not equal, return the index of
#     the first difference. If the contents of the two lists
#     are equal, return -1.

#     Parameters
#         list1: a list
#         list2: another list
#     Return: an index or -1
#     """
#     # Get the length of the shortest list.
#     length1 = len(list1)
#     length2 = len(list2)
#     limit = min(length1, length2)

#     # Begin at the first index (0) and repeat until the
#     # computer finds two elements that are not equal or
#     # until the computer reaches the end of the shortest
#     # list, whichever comes first.
#     i = 0
#     while i < limit:
#         # Retrieve one element from each list.
#         element1 = list1[i]
#         element2 = list2[i]

#         # If the two elements are not
#         # equal, quit the while loop.
#         if element1 != element2:
#             break

#         # Add one to the index variable.
#         i += 1

#     # If the length of both lists are equal and the
#     # computer verified that all elements are equal,
#     # set i to -1 to indicate that the contents of
#     # the two lists are equal.
#     if length1 == length2 == i:
#         i = -1

#     return i


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# # Example 8

# def main():
#     # These are the indexes of each
#     # element in the inner lists.
#     YEAR_PLANTED_INDEX = 0
#     HEIGHT_INDEX = 1
#     GIRTH_INDEX = 2
#     FRUIT_AMOUNT_INDEX = 3

#     # Create a compound list that stores inner lists.
#     apple_tree_data = [
#         # [year_planted, height, girth, fruit_amount]
#         [2012, 2.7, 3.6, 70.5],
#         [2012, 2.4, 3.7, 81.3],
#         [2015, 2.3, 3.6, 62.7],
#         [2016, 2.1, 2.7, 42.1]
#     ]

#     # Retrieve one inner list from the compound list.
#     one_tree = apple_tree_data[2]

#     # Retrieve one value from the inner list.
#     height = one_tree[HEIGHT_INDEX]

#     # Print the tree's height.
#     print(f"height: {height}")


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# # Example 9

# def main():
#     # These are the indexes of each
#     # element in the inner lists.
#     YEAR_PLANTED_INDEX = 0
#     HEIGHT_INDEX = 1
#     GIRTH_INDEX = 2
#     FRUIT_AMOUNT_INDEX = 3

#     # Create a compound list that stores inner lists.
#     apple_tree_data = [
#         # [year_planted, height, girth, fruit_amount]
#         [2012, 2.7, 3.6, 70.5],
#         [2012, 2.4, 3.7, 81.3],
#         [2015, 2.3, 3.6, 62.7],
#         [2016, 2.1, 2.7, 42.1]
#     ]

#     total_fruit_amount = 0

#     # This loop will repeat once for each inner list
#     # in the apple_tree_data compound list.
#     for inner_list in apple_tree_data:

#         # Retrieve the fruit amount from
#         # the current inner list.
#         fruit_amount = inner_list[FRUIT_AMOUNT_INDEX]

#         # Print the fruit amount for the current tree.
#         print(fruit_amount)

#         # Add the current fruit amount to the total.
#         total_fruit_amount += fruit_amount

#     # Print the total fruit amount.
#     print(f"Total fruit amount: {total_fruit_amount:.1f}")


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# # Example 10

# def main():
#     x = 17
#     y = x
#     print(f"Before changing x: x {x}  y {y}")
#     x += 1
#     print(f"After changing x:  x {x}  y {y}")

# # Call main to start this program.
# if __name__ == "__main__":
#     main()



# # Example 11

# def main():
#     lx = [7, -2]
#     ly = lx
#     print(f"Before changing lx: lx {lx}  ly {ly}")
#     lx.append(5)
#     print(f"After changing lx:  lx {lx}  ly {ly}")

# # Call main to start this program.
# if __name__ == "__main__":
#     main()

RADIUS_INDEX = 0

bad_guys = {
    "daredevil" : [6.83, 10.16],
    "x-men" : [7.78, 11.91],
    "batman" : "bane"
}

print(bad_guys)

radius = (bad_guys.get("daredevil", [RADIUS_INDEX]))

# print(bad_guys["batman"])

# bad_guys["deadpool"] = "evil deadpool"

# print(bad_guys)

# bad_guys["x-men"] = "juggernaut"

# del bad_guys["deadpool"]

# print(bad_guys)



# geeky_list = ["geek", "GeeksforGeeks", "geeky", "geekgod"]
# # index = 1
# print(geeky_list.index("GeeksforGeeks"))

# # Example 2

# import csv

# def main():
#     # Open the CSV file for reading and store a reference
#     # to the opened file in a variable named csv_file.
#     with open("hymns.csv", "rt") as csv_file:

#         # Use the csv module to create a reader object
#         # that will read from the opened CSV file.
#         reader = csv.reader(csv_file)

#         # Read the rows in the CSV file one row at a time.
#         # The reader object returns each row as a list.
#         for row_list in reader:
#             print(row_list)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# # Example 3

# import csv

# # Indexes of some of the columns
# # in the dentists.csv file.
# COMPANY_NAME_INDEX = 0
# NUM_EMPS_INDEX = 3
# NUM_PATIENTS_INDEX = 4


# def main():
#     # Open a file named dentists.csv and store a reference
#     # to the opened file in a variable named dentists_file.
#     with open("dentists.csv", "rt") as dentists_file:

#         # Use the csv module to create a reader
#         # object that will read from the opened file.
#         reader = csv.reader(dentists_file)
        
#         # The first row of the CSV file contains column
#         # headings and not data about a dental office,
#         # so this statement skips the first row of the
#         # CSV file.
#         next(reader)

#         running_max = 0
#         most_office = None

#         # Read each row in the CSV file one at a time.
#         # The reader object returns each row as a list.
#         for row_list in reader:

#             # For the current row, retrieve the
#             # values in columns 0, 3, and 4.
#             company = row_list[COMPANY_NAME_INDEX]
#             num_employees = int(row_list[NUM_EMPS_INDEX])
#             num_patients = int(row_list[NUM_PATIENTS_INDEX])

#             # Compute the number of patients per
#             # employee for the current dental office.
#             patients_per_emp = num_patients / num_employees

#             # If the current dental office has more
#             # patients per employee than the running
#             # maximum, assign running_max and most_office
#             # to be the current dental office.
#             if patients_per_emp > running_max:
#                 running_max = patients_per_emp
#                 most_office = company

#     # Print the results for the user to see.
#     print(f"{most_office} has {running_max:.1f}"
#             " patients per employee")


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# # Example 4

# import csv

# def main():
#     # Read the contents of the dentists.csv file
#     # into a compound list.
#     dentists_list = read_compound_list("dentists.csv")

#     # Print the entire list.
#     print(dentists_list)


# def read_compound_list(filename):
#     """Read the contents of a CSV file into a compound
#     list and return the list. Each element in the
#     compound list will be a small list that contains
#     the values from one row of the CSV file.

#     Parameter filename: the name of the CSV file to read
#     Return: a list of lists that contain strings
#     """
#     # Create an empty list that will
#     # store the data from the CSV file.
#     compound_list = []

#     # Open the CSV file for reading and store a reference
#     # to the opened file in a variable named csv_file.
#     with open(filename, "rt") as csv_file:

#         # Use the csv module to create a reader object
#         # that will read from the opened CSV file.
#         reader = csv.reader(csv_file)

#         # Read the rows in the CSV file one row at a time.
#         # The reader object returns each row as a list.
#         for row_list in reader:

#             # If the current row is not blank,
#             # append it to the compound_list.
#             if len(row_list) != 0:

#                 # Append one row from the CSV
#                 # file to the compound list.
#                 compound_list.append(row_list)

#     # Return the compound list.
#     return compound_list


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# # Example 5

# import csv


# def main():
#     # Index of the phone number column
#     # in the dentists.csv file.
#     PHONE_INDEX = 2

#     # Read the contents of the dentists.csv into a
#     # compound dictionary named dentists_dict. Use
#     # the phone numbers as the keys in the dictionary.
#     dentists_dict = read_dictionary("dentists.csv", PHONE_INDEX)

#     # Print the dentists compound dictionary.
#     print(dentists_dict)


# def read_dictionary(filename, key_column_index):
#     """Read the contents of a CSV file into a compound
#     dictionary and return the dictionary.

#     Parameters
#         filename: the name of the CSV file to read.
#         key_column_index: the index of the column
#             to use as the keys in the dictionary.
#     Return: a compound dictionary that contains
#         the contents of the CSV file.
#     """
#     # Create an empty dictionary that will
#     # store the data from the CSV file.
#     dictionary = {}

#     # Open the CSV file for reading and store a reference
#     # to the opened file in a variable named csv_file.
#     with open(filename, "rt") as csv_file:

#         # Use the csv module to create a reader object
#         # that will read from the opened CSV file.
#         reader = csv.reader(csv_file)

#         # The first row of the CSV file contains column
#         # headings and not data, so this statement skips
#         # the first row of the CSV file.
#         next(reader)

#         # Read the rows in the CSV file one row at a time.
#         # The reader object returns each row as a list.
#         for row_list in reader:

#             # If the current row is not blank, add the
#             # data from the current to the dictionary.
#             if len(row_list) != 0:

#                 # From the current row, retrieve the data
#                 # from the column that contains the key.
#                 key = row_list[key_column_index]

#                 # Store the data from the current
#                 # row into the dictionary.
#                 dictionary[key] = row_list

#     # Return the dictionary.
#     return dictionary


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# # Example 6

# def main():
#     # Create a list that contains country names
#     # and print the list.
#     countries = [
#         "Canada", "France", "Ghana", "Brazil", "Japan"
#     ]

#     print(countries)

#     # Sort the list. Then print the sorted list.
#     sorted_list = sorted(countries)
#     print(sorted_list)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()

# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)
# f(0)


from datetime import datetime

obj = datetime.now()

year = obj.year
new_obj = obj.replace(year=2035)
new_obj = new_obj.year
day_of_Week = obj.weekday()

print(new_obj)
print(day_of_Week)