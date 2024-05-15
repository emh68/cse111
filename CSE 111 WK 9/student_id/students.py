
import csv

def main():
    STUDENT_NUMBER_INDEX = 0
    STUDENT_NAME_INDEX = 1
    students_dict = read_dictionary("students.csv", STUDENT_NUMBER_INDEX)
    # print(students_dict)
    
    student_number = input("Please enter a student number (xxxxxxxxx): ")
    student_number = student_number.replace("-", "")

    if not student_number.isdigit():
        print("Invalid character please enter only numbers.")

    else:
        if len(student_number) < 9:
            print("Invalid student number: too few digits")
        elif len(student_number) > 9:
            print("Invalid student number: too many digits")
        else:
            # Find the student number in the list of numbers.
            if student_number not in students_dict:
                print("No such student")

            else:
                number = students_dict[student_number]
                name = number[STUDENT_NAME_INDEX]

                print(name)

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
    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]

                dictionary[key] = row_list

    return dictionary


# def check_student(student_number, key_column_index):
#     for student_number in key_column_index:
#         if student_number == key_column_index[0]:


if __name__ == "__main__":
    main()