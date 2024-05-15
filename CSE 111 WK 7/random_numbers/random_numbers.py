

import random


def main():
    # list of numbers
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")

    # add a number to the numbers list then print
    append_random_numbers(numbers)
    print(f"numbers {numbers}")

    # add 3 more numbers to the numbers list then print
    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")

    # create empty words list
    words = []

    # add a word to words list and print list
    append_random_words(words)
    print(f"words {words}")

    # add 7 words to the words list and print the list
    append_random_words(words, 7)
    print(f"words {words}")


def append_random_numbers(numbers_list, quantity=1):
    """Randomly choose numbers and add them onto the numbers list.
    The random numbers are between 0 and 100, inclusive.
    Parameters
        numbers_list: A list of numbers where this function will
            append random numbers.
        quantity: The number of random numbers that this function
            will append onto numbers_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the numbers_list.
    """
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        random_number = round(random_number, 1)
        numbers_list.append(random_number)


def append_random_words(words_list, quantity=1):
    """Randomly choose words and add them onto the words list.
    Parameters
        words_list: A list of words where this function will
            append random words.
        quantity: The number of random words that this function
            will append onto words_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the words_list.
    """

    # A list of words to randomly choose from.
    words = [
        "hydrogen", "sleep", "speak", "sunshine", "toothbrush",
        "tree", "truth", "walk", "water", "warrant", "decide",
        "architecture", "constraint", "gutter", "recycle", "office",
        "drum", "color", "develop", "sin", "car", "composer",
        "microphone", "driver", "relative", "year", "drop",
        "warning", "organisation", "snail", "cutting", "proposal",
        "excavate", "projection", "love", "book", "dinner", "scan",
        "cultivate", "silk", "democratic", "mechanical", "budge",
        "confuse", "winter", "excitement", "thick"
    ]

    # Randomly choose quantity words and append them onto words_list.
    for _ in range(quantity):
        word = random.choice(words)
        words_list.append(word)


if __name__ == "__main__":
    main()
