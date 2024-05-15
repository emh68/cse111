from names import make_full_name, extract_given_name, extract_family_name
import pytest


def test_make_full_name():
    
    assert make_full_name("Marie", "Toussaint") == "Toussaint; Marie"
    assert make_full_name("Fred", "Jones") == "Jones; Fred"
    assert make_full_name("John", "Caldwell-Pope") == "Caldwell-Pope; John"
    assert make_full_name("", "") == "; "


def test_extract_family_name():

    assert extract_family_name("Toussaint; Marie") == "Toussaint"
    assert extract_family_name("Jones; Fred") == "Jones"
    assert extract_family_name("Caldwell-Pope; John") == "Caldwell-Pope"
    assert extract_family_name("; ") == ""


def test_extract_given_name():

    assert extract_given_name("Toussaint; Marie") == "Marie"
    assert extract_given_name("Jones; Fred") == "Fred"
    assert extract_given_name("Caldwell-Pope; John") == "John"
    assert extract_given_name("; ") == ""


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
