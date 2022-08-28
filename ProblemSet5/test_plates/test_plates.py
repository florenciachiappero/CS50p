# In a file called test_plates.py, implement four or more functions that
# collectively test your implementation of is_valid thoroughly.

from plates import is_valid

def main():
    # Call test functions
    test_min_max()
    test_two_letters()
    test_middle()
    test_first_number()
    test_punctuation()
    
# Plates may contain a maximum of 6 characters(letters or numbers) and a minimum or 2 characters
def test_min_max():
    assert is_valid('AA') == True
    assert is_valid('ABDCEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFGH') == False

# Plates must start with at least two letters
def test_two_letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False

# Numbers cannot be used in the middle of a plate; they must come at the end
def test_middle():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False

# The first number used cannot be a '0'
def test_first_number():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

# No periods, spaces, or punctuation marks are allowed
def test_punctuation():
    assert is_valid('PI3.14') == False
    assert is_valid('PI3!14') == False
    assert is_valid('PI 14') == False

if __name__ == "__main__":
    main()