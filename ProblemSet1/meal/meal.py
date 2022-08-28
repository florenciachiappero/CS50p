# In meal.py, implement a program that prompts the user for a time and 
# outputs whether it’s breakfast time, lunch time, or dinner time. If 
# it’s not time for a meal, don’t output anything at all. Assume that 
# the user’s input will be formatted in 24-hour time as #:## or ##:##. 
# And assume that each meal’s time range is inclusive. For instance, 
# whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s 
# time for breakfast.

def main():
    # Input from the user
    time = input('What time is it? ')

    # Call the convert function
    time_converted = convert(time)

    # Conditional for breakfast, lunch and dinner
    if time_converted >= 7 and time_converted <= 8:
        print('breakfast time')
    if time_converted >= 12 and time_converted <= 13:
        print('lunch time')
    if time_converted >= 18 and time_converted <= 19:
        print('dinner time')


def convert(time):
    hours, minutes = time.split(':')
    f_minutes = float(minutes) / 60
    f_hours = float(hours)
    return f_hours + f_minutes


if __name__ == "__main__":
    main()