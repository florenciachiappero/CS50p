# In a file called test_numb3rs.py, two or more functions that 
# collectively test your implementation of validate thoroughly.

from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate('1.2.3.4') == True
    assert validate('1.2.3') == False
    assert validate('1.2') == False
    assert validate('1') == False
    assert validate('cat') == False

def test_range():
    assert validate('255.255.255.255') == True
    assert validate('127.0.0.1') == True
    assert validate('512.512.512.512') == False
    assert validate('512.1.1.1') == False
    assert validate('1.512.1.1') == False
    assert validate('1.1.1.512') == False
    assert validate('1.1.512.1') == False

if __name__ == "__main__":
    main()