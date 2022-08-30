# In a file called scourgify.py, implement a program that:
# Expects the user to provide two command-line arguments:
    # the name of an existing CSV file to read as input, whose columns 
    # are assumed to be, in order, name and house, and
    # the name of a new CSV to write as output, whose columns should be, 
    # in order, first, last, and house.
# Converts that input to that output, splitting each name into a first 
# name and last name. Assume that each student will have both a first 
# name and last name.


import sys
import csv

def main():
    # Check command line arguments
    check_command_line_arg()

    # Create a list to store data from the first csv file
    output = []
    open_file(output)

    # Write CSV file
    write_CSVfile(output)


def check_command_line_arg():
    # Check how many elements in the command line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check if it is a CSV file
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV File")


def open_file(output):
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                split_name = row["name"].split(",")
                output.append({'first': split_name[1].lstrip(), 'last': split_name[0], 'house': row['house']})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    return output


def write_CSVfile(output):
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


if __name__ == "__main__":
    main()