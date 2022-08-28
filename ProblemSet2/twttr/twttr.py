# In a file called twttr.py, implement a program that prompts the user 
# for a str of text and then outputs that same text but with all vowels 
# (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

# Get user input
answer = input("Input: ")

output = ""

# Loop through every letter
for i in range (len(answer)):
    if not answer[i].lower() in ['a', 'e', 'i', 'o', 'u']:
        output += answer[i]


# Print "Output: "
print("Output:", output)