import sys
import random
from pyfiglet import Figlet

figlet = Figlet()


def main():
    input_font = check_argv()
    get_font(input_font)

    # Get user input to change the font
    message = input("Input: " )

    # Print message
    print(f"Output: {figlet.renderText(message)}")



def check_argv():
    if len(sys.argv) == 1:
        return True
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        return False
    else: 
        sys.exit(1)


def get_font(f):
    if f == False :
        try:
            return figlet.setFont(sys.argv[2])
        except:
            print("Invalid usage")
            sys.exit (1)
    else:
        return random.choice(figlet.getFonts())


if __name__ == "__main__":
    main()
    

                     
