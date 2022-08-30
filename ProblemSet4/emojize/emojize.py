# In a file called emojize.py, implement a program that prompts the user 
# for a str in English and then outputs the “emojized” version of that 
# str, converting any codes (or aliases) therein to their corresponding 
# emoji.

import emoji

# Get user input
user_input = input("Input: ")

# Convert input into an emoji
output = emoji.emojize(user_input)

# Print output
print("Output: ", output)