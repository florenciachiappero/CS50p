# In a file called test_bank.py, implement three or more functions that 
# collectively test your implementation of value thoroughly.

from bank import value

def main():
    # Call test functions
    test_0()
    test_20()
    test_100()

# Test return 0
def test_0():
    assert value('Hello') == 0
    assert value('hello Florencia') == 0

# Test return 20
def test_20():
    assert value('Hi') == 20
    assert value('how are you today?') == 20

# Test return 100
def test_100():
    assert value('Good morning') == 100
    assert value('whats good?') == 100

if __name__ == "__main__":
    main()