# In a file called twttr.py, reimplement Setting up my twttr from Problem 
# Set 2, restructuring your code per the below, wherein shorten expects 
# a str as input and returns that same str but with all vowels 
# (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    # Get user input
    answer = input("Input: ")

    # Remove all vowels
    output = shorten(answer)

    # Print output
    print("Output: ", output)

def shorten(word):
    word_no_vowels = ""

    # Loop through every letter
    for i in range (len(word)):
    if not word[i].lower() in ['a', 'e', 'i', 'o', 'u']:
        word_no_vowels += word[i]
    return word_no_vowels

if __name__ == "__main__":
    main()

