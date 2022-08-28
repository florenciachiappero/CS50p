# In a file called fuel.py, implement a program that prompts the user for 
# a fraction, formatted as X/Y, wherein each of X and Y is an integer, 
# and then outputs, as a percentage rounded to the nearest integer, how 
# much fuel is in the tank. If, though, 1% or less remains, output E 
# instead to indicate that the tank is essentially empty. And if 99% or 
# more remains, output F instead to indicate that the tank is essentially 
# full.

# Be sure to catch any exceptions like ValueError or ZeroDivisionError.


def main():

    # Gets user input, checks it for errors and returns the fraction.
    fuel = get_fuel()

    # Prints output
    print(output(fuel))


def get_fuel():
    while True:
        # Get user input
        fuel = input("Fraction: ")

        # Check input for errors
        try:
            n, d = fuel.split("/")
            numerator = int(n)
            denominator = int(d)

            # Calculate the fraction between n / d
            f = round(numerator / denominator, 2)

            # Check if its less than 1 and stop the loop
            if f <= 1:
                return f

        except (ValueError, ZeroDivisionError):
            pass


def output(f):

    # Multiply percentage by 100
    p = int(f * 100)

    # Check if percentage is less than 1, print E
    if p <= 1:
        return("E")

    # Check if percentage is greater than 99, print F
    if p >= 99:
        return("F")

    # Otherwise, print the %
    else:
        return(f"{p}%")


if __name__ == "__main__":
    main()