from address import extract_city, extract_state, extract_zipcode
import pytest


def test_extract_city():
    
    assert extract_city("15336 S Oriskany Ln, Bluffdale, UT 84065") == "Bluffdale"
    # assert extract_city("Fred", "Jones") == "Jones; Fred"
    # assert extract_city("John", "Caldwell-Pope") == "Caldwell-Pope; John"
    # assert extract_city("", "") == "; "


def test_extract_state():

    assert extract_state("15336 S Oriskany Ln, Bluffdale, UT 84065") == "UT"
    # assert extract_state("Jones; Fred") == "Jones"
    # assert extract_state("Caldwell-Pope; John") == "Caldwell-Pope"
    # assert extract_state("; ") == ""


def test_extract_zipcode():

    assert extract_zipcode("15336 S Oriskany Ln, Bluffdale, UT 84065") == "84065"
    # assert extract_zipcode("Jones; Fred") == "Fred"
    # assert extract_zipcode("Caldwell-Pope; John") == "John"
    # assert extract_zipcode("; ") == ""


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

