

def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    provinces_list = read_list("provinces.txt")

    # Print original list.
    print(provinces_list)

    # Remove first element from list.
    provinces_list.pop(0)

    # Remove last element from list.
    provinces_list.pop()

    # Replace "AB" with "Alberta"
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
    print(provinces_list)

    count = provinces_list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list.")
    print()


def read_list(provinces):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    provinces_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(provinces, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            provinces_list.append(clean_line)

    # Return the list that contains the lines of text.
    return provinces_list


# Call main to start this program.
if __name__ == "__main__":
    main()
