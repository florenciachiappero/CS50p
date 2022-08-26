# In a file called playback.py, implement a program in Python that prompts
# the user for input and then outputs that same input, replacing each 
# space with ... (i.e., three periods).


# Get input from the user
text = input()

# Change whitespace for 3 dots
new_text = text.replace(" ", "...")

# Print output
print(new_text)