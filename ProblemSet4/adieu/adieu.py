# In a file called adieu.py, implement a program that prompts the user 
# for names, one per line, until the user inputs control-d. Assume that 
# the user will input at least one name. Then bid adieu to those names, 
# separating two names with one and, three names with two commas and one 
# and, and  names with n-1 commas and one and.


import inflect

p = inflect.engine()

# Create list to keep track of names
names = []


while True:
    try:
        # Get user input
        name = input("Name: ")
        names.append(name)
    except EOFError:
        # Create new line and stop the loop
        print()
        break

# Printing using inflect module
output = p.join(names)
print("Adieu, adieu, to " + output)