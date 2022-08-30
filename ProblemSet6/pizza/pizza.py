# In a file called pizza.py, implement a program that expects exactly one 
# command-line argument, the name (or path) of a CSV file in Pinocchio’s 
# format, and outputs a table formatted as ASCII art using tabulate, a 
# package on PyPI at pypi.org/project/tabulate. Format the table using 
# the library’s grid format. If the user does not specify exactly one 
# command-line argument, or if the specified file’s name does not end in 
# .csv, or if the specified file does not exist, the program should 
# instead exit via sys.exit.

import sys
import csv
from tabulate import tabulate


def main():
    check_command_line_arg()

    # Create variable to store the table data
    table = []
    get_table(table)

    # Print the table
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))



def check_command_line_arg():
    # Check how many elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check if it is a CSV file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


def get_table(table):
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

    return table


if __name__ == "__main__":
    main()