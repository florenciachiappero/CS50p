from fuel import convert, gauge
import pytest

def main():
    # Call test functions
    test_value()
    test_zero_division()
    test_correct_input()


# Test ValueError
def test_value():
    with pytest.raises(ValueError):
        convert('cat/dog')

# Test ZeroDivisionError
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

# Test correct input
def test_correct_input():
    assert convert('2/3') == 67 and gauge(67) =='67%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'


if __name__ == "__main__":
    main()