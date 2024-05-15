
"""This program attempts to create a simple sentence using determiner(s)/article(s), 
nouns, adverbs, verbs and prepositional phrases. For this assignment I exceeded the requirements 
by adding a 2nd prepositional phrase and by adding an adverb function and calling the function. """


import random


def main():
    quantity = random.randint(0, 1)

    tense_list = ["past", "present", "future"]
    tense = random.choice(tense_list)

    make_sentence(1, "past")
    make_sentence(1, "present")
    make_sentence(1, "future")
    make_sentence(0, "past")
    make_sentence(0, "present")
    make_sentence(0, "future")


def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    print(f"{get_determiner(quantity).capitalize()} {get_noun(quantity)} {get_adverb()} "
          f"{get_verb(quantity, tense)} {get_prepositional_phrase(quantity)} {get_determiner(quantity)} "
          f"{get_noun(quantity)} {get_prepositional_phrase(quantity)}.")


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """

    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    noun = random.choice(words)
    return noun


def get_verb(quantity, tense):
    # Conditions for which verb list to choose.
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]

    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]

    elif tense == "present" and not quantity == 1:
        words = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]

    else:
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]

    # Randomly choose and return a verb.
    verb = random.choice(words)
    return verb


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """

    words = ["about", "above", "across", "after", "along", "around", "at",
             "before", "behind", "below", "beyond", "by", "despite", "except",
             "for", "from", "in", "into", "near", "of", "off", "on", "onto",
             "out", "over", "past", "to", "under", "with", "without"]

    preposition = random.choice(words)
    return preposition


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    prepositional_phrase = f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"
    return prepositional_phrase


def get_adverb():
    # Get an adverb from a list of adverbs

    words = ["often", "quickly", "slowly", "boldly", "happily", "calmly", "certainly", "cheerfully",
             "extremely", "sadly", "wildly", "abnormally", "awkwardly", "bashfully", "hardly ever",
             "occasionally", "generally", "normally", "loosely", "loudly", "madly", "mockingly",
             "more", "mostly", "nearly", "naturally", "nervously", "never", "nicely", "optimistically",
             "painfully", "perfectly", "patiently", "playfully", "politely", "positively", "promptly",
             "quickly", "quietly", "silently", "solemnly", "sometimes", "usually"]

    adverb = random.choice(words)
    return adverb


main()
