"""This code asks a series of questions and then calculates your 
self-esteem score based on the Rosenberg Self-Esteem Scale and 
your nature relatedness score"""


def main():

    print("This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten\n"
          "statements that you could possibly apply to yourself. Please rate how much you agree with each of the\n"
          "statements by responding with one of these four letters:")
    print()
    print("D = strongly disagree with the statement.\n"
          "d = somewhat disagree with the statement.\n"
          "a = somewhat agree with the statement.\n"
          "A = strongly agree with the statement.")
    print()

    rosenberg_score = 0
    rosenberg_score += ask_positive_question(
        "1. I feel that I am a person of worth, at least on an"
        " equal plane with others.")
    rosenberg_score += ask_positive_question(
        "2. I feel that I have a number of good qualities.")
    rosenberg_score += ask_negative_question(
        "3. All in all, I am inclined to feel that I am a failure.")
    rosenberg_score += ask_positive_question(
        "4. I am able to do things as well as most other people.")
    rosenberg_score += ask_negative_question(
        "5. I feel I do not have much to be proud of.")
    rosenberg_score += ask_positive_question(
        "6. I take a positive attitude toward myself.")
    rosenberg_score += ask_positive_question(
        "7. On the whole, I am satisfied with myself.")
    rosenberg_score += ask_negative_question(
        "8. I wish I could have more respect for myself.")
    rosenberg_score += ask_negative_question(
        "9. I certainly feel useless at times.")
    rosenberg_score += ask_negative_question(
        "10. At times I think I am no good at all.")

    nature_score = 0
    nature_score += nature_related_scale(
        "11. My ideal vacation spot would be a remote, wilderness area.")
    nature_score += nature_related_scale(
        "12. I always think about how my actions affect the environment.")
    nature_score += nature_related_scale(
        "13. My connection to nature and the environment is a part of my spirituality.")
    nature_score += nature_related_scale(
        "14. I take notice of wildlife wherever I am.")
    nature_score += nature_related_scale(
        "15. My relationship to nature is an important part of who I am.")
    nature_score += nature_related_scale(
        "16. I feel very connected to all living things and the earth.")

    nature_score = nature_score / 6

    print()
    print(f"Your Rosenberg self-esteem score is {rosenberg_score}")
    print("A score below 15 may indicate problematic low self-esteem.")

    print()
    print(f"Your nature relatedeness score is {nature_score}")
    # print("A score below 15 may indicate problematic low self-esteem.")


def ask_positive_question(statement):
    """Display one statement to the user and get the user's response.
    Then determine the score for the response and return the score.

    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    print(statement)
    answer = input("   Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 0
    elif answer == 'd':
        score = 1
    elif answer == 'a':
        score = 2
    elif answer == 'A':
        score = 3
    return score


def ask_negative_question(statement):
    """Display one statement to the user and get the user's response.
    Then determine the score for the response and return the score.

    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    print(statement)
    answer = input("Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 3
    elif answer == 'd':
        score = 2
    elif answer == 'a':
        score = 1
    elif answer == 'A':
        score = 0
    return score


def nature_related_scale(statement):

    print(statement)
    answer = input("Enter 1, 2, 3, 4 or 5: ")
    nature_score = 0

    if answer == "1":
        nature_score = 1
    elif answer == "2":
        nature_score = 2
    elif answer == "3":
        nature_score = 3
    elif answer == "4":
        nature_score = 4
    elif answer == "5":
        nature_score = 5
    return nature_score


if __name__ == "__main__":
    main()
