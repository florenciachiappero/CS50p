# In a file called shirt.py, implement a program that expects exactly two
# command-line arguments:
    # in sys.argv[1], the name (or path) of a JPEG or PNG to read 
    # (i.e., open) as input
    # in sys.argv[2], the name (or path) of a JPEG or PNG to write 
    # (i.e., save) as output
# The program should then overlay shirt.png (which has a transparent 
# background) on the input after resizing and cropping the input to be 
# the same size, saving the result as its output.

import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arg()

    # Open the image
    try:
        imageFile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Open shirt
    shirtfile = Image.open("shirt.png")

    # Get the size of the shirt
    size = shirtfile.size

    # Resize muppet image ti fit shirt
    muppet = ImageOps.fit(imageFile, size)

    # Paste shirt in muppet
    muppet.paste(shirtfile, shirtfile)

    # Create output image
    muppet.save(sys.argv[2])

def check_command_line_arg():
    # Check how many elements in the command line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    # Check if it is a image file
    if check_extension(file1[1]) == False:
        sys.exit("Invalid input")
    if check_extension(file2[1]) == False:
        sys.exit("Invalid output")

    # Check if extension of both files are the same
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")


def check_extension(file):
    if file in [".jpg" , ".jpeg", ".png"]:
        return True
    return False


if __name__ == "__main__":
    main()