# In a file called bank.py, reimplement Home Federal Savings Bank from 
# Problem Set 1, restructuring your code per the below, wherein value 
# expects a str as input and returns 0 if that str starts with “hello”, 
# 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, 
# treating the str case-insensitively. Only main should call print.

def main():
    # Get user input
    greeting = input("Greeting: ")

    # Print greeting value
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.lower().strip()

    # Check if the answer has ' hello', return 0
    if 'hello' in greeting:
        return 0
    # Check if answer start with 'h', return 20
    elif 'h' == greeting[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()