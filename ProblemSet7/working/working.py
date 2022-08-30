# In a file called working.py, implement a function called convert that 
# expects a str in either of the 12-hour formats below and returns the 
# corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that 
# AM and PM will be capitalized (with no periods therein) and that there 
# will be a space before each. Assume that these times are representative 
# of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    rightFormat = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if rightFormat:
        pieces = rightFormat.groups()
        if int(pieces[1]) > 12 or int(pieces[5]) > 12:
            raise ValueError
        first_time = new_format(pieces[1], pieces[2], pieces[3])
        second_time = new_format(pieces[5], pieces[6], pieces[7])
        return first_time + ' to ' + second_time
    else:
        raise ValueError

def new_format(hour, minute, am_pm):
    if am_pm == 'PM':
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)

    if minute == None:
        new_min = ':00'
        new_time = f"{new_hour:02}" + new_min
    else:
        new_time = f"{new_hour:02}" + ":" + minute
    return new_time


if __name__ == "__main__":
    main()