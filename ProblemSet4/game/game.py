# In a file called game.py, implement a program that:

# Prompts the user for a level, . If the user does not input a positive 
# integer, the program should prompt again.
# Randomly generates an integer between 1 and , inclusive, using the 
# random module.
# Prompts the user to guess that integer. If the guess is not a positive 
# integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output 
# Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output 
# Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output 
# Just right! and exit.


import random

def main():
    level = get_level()

    # Set random number
    random_n = random.randint(1, level)

    # Print result
    print(game(random_n))


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except:
            pass


def game(r_n):
    # Get guess and check
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < r_n:
                    print("Too small!")
                    pass
                elif guess > r_n:
                    print("Too large!")
                    pass
                else:
                    return "Just right!"
        except:
            pass


if __name__ == "__main__":
    main()