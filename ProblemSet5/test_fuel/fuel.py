def main():

    # Gets user input
    fraction = input("Fraction: ")

    percentage = convert(fraction)
    # Prints output
    print(gauge(percentage))


def convert(fraction):
    while True:

        # Check input for errors
        try:
            n, d = fraction.split("/")
            numerator = int(n)
            denominator = int(d)

            # Calculate the fraction between n / d
            f = round(numerator / denominator, 2)

            # Check if its less than 1 and stop the loop
            if f <= 1:
                p = int(f * 100)
                return p

            # Reprompt user for input
            else:
                fraction = input("Fraction: ")
                pass

        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):

    # Check if percentage is less than 1, print E
    if percentage <= 1:
        return("E")

    # Check if percentage is greater than 99, print F
    if percentage >= 99:
        return("F")

    # Otherwise, print the %
    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()