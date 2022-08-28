# In a file called camel.py, implement a program that prompts the user 
# for the name of a variable in camel case and outputs the corresponding 
# name in snake case. Assume that the user’s input will indeed be in camel
# case.

# Get user input
camelCase = input("camelCase: ")

snake_case = ""

# Loop through every letter
for i in range(len(camelCase)):
    if camelCase[i].isupper():
        snake_case += '_' + camelCase[i].lower()
    else:
        snake_case += camelCase[i]

# Print snake_case
print("snake_case: ", snake_case)