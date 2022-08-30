# In a file called lines.py, implement a program that expects exactly one 
# command-line argument, the name (or path) of a Python file, and outputs 
# the number of lines of code in that file, excluding comments and blank 
# lines. If the user does not specify exactly one command-line argument, 
# or if the specified file’s name does not end in .py, or if the 
# specified file does not exist, the program should instead exit via 
# sys.exit.

# Assume that any line that starts with #, optionally preceded by 
# whitespace, is a comment. (A docstring should not be considered a 
# comment.) Assume that any line that only contains whitespace is blank.


import sys


def main():
    check_command_line_arg()

    # Print the amount of lines
    count = open_and_count()
    print(count)



def check_command_line_arg():

    # Check how many elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check if it is a Python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")



def open_and_count():
    count = 0

    # Try to open the file
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()

        # Count lines that are not comments or blank
        for line in lines:
            if check_line(line) == False:
                count += 1
        return count

    except FileNotFoundError:
        sys.exit("File does not exist")



def check_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False



if __name__ == "__main__":
    main()