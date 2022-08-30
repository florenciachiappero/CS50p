# In a file called test_um.py, three or more functions that collectively 
# test your implementation of count thoroughly.

from um import count

def main():
    test_upper_lower()
    test_word()
    test_space()

def test_upper_lower():
    assert count('Um, thanks for the album') == 1
    assert count('Um, thanks, um...') == 2

def test_word():
    assert count('yummy') == 0

def test_space():
    assert count('Hello um world') == 1
    assert count('um?') == 1

if __name__ == "__main__":
    main()