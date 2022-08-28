# In a file called plates.py, reimplement Vanity Plates from Problem Set 2, 
# restructuring your code per the below, wherein is_valid still expects a str as 
# input and returns True if that str meets all requirements and False if it does 
# not, but main is only called if the value of __name__ is "__main__":

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    # Vanity plates may contain a maximum of 6 characters (letter or numbers)
    # and a minimum of 2 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # All vanity plates must start with at least two letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # AAA22A would not be acceptable
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    # The first number used cannot be a 0
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

    # No periods, spaces, or punctuation marks are allowed
    for c in s:
        if c in ['.', ' ', '!', '?']:
            return False

    # If we pass all the tests, return True
    return True


if __name__ == "__main__":
    main()