# In a file called bank.py, implement a program that prompts the user for 
# a greeting. If the greeting starts with “hello”, output $0. If the 
# greeting starts with an “h” (but not “hello”), output $20. Otherwise, 
# output $100. Ignore any leading whitespace in the user’s greeting, and 
# treat the user’s greeting case-insensitively.

# Get user input
answer = input("Greeting: ").lower().strip()

# Check if the answer has "hello", print $0
if 'hello' in answer:
    print("$0")
# Check if answer starts with "h", print $20
elif 'h' == answer[0]:
    print("$20")
# Otherwise, print $100
else:
    print("$100")