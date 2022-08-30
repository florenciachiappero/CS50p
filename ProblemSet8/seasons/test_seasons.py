# In a file called test_seasons.py, one or more functions that test your 
# implementation of any functions besides main in seasons.py thoroughly.

from seasons import check_birthday

def main():
    test_check_birthday()


def test_check_birthday():
    assert check_birthday('1998-07-03') == ("1998", "07", "03")
    assert check_birthday('1998-7-3') == None

if __name__ == "__main__":
    main()