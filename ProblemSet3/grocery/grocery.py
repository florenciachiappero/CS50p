# In a file called grocery.py, implement a program that prompts the user 
# for items, one per line, until the user inputs control-d (which is a 
# common way of ending one’s input to a program). Then output the user’s 
# grocery list in all uppercase, sorted alphabetically by item, prefixing 
# each line with the number of times the user inputted that item. No need 
# to pluralize the items. Treat the user’s input case-insensitively.


grocery = {}

while True:
    try:
        # Get user input
        item = input()

        # Check if item is in the dictionary
        if item in grocery:
            grocery[item] += 1

        # Otherwise, add item to the dictionary
        else:
            grocery[item] = 1

    except EOFError:
        # Print all the items in alphabetical order
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        break