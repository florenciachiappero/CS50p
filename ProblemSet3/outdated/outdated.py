# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order.

# Create list with the name of all months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    # Get user input
    date = input("Date: ")

    try:
        month, day, year = date.split("/")

        # Check if 1 <= month <= 12 and 1 <= day <= 31
        if int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
            break

    except:
        try:
            m, d, year = date.split(" ")

            # Check if the month exist according to our list
            for i in range(len(months)):
                if m == months[i]:
                    month = i + 1

            # Replace the comma from the day
            day = d.replace(",","")

            # Check if 1 <= month <= 12 and 1 <= day <= 31
            if int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
                break

        except:
            print()
            pass

# Print the date in the expected format
print(f"{year}-{int(month):02}-{int(day):02}")