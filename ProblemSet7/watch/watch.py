# In a file called watch.py, implement a function called parse that 
# expects a str of HTML as input, extracts any YouTube URL that’s the 
# value of a src attribute of an iframe element therein, and returns its 
# shorter, shareable youtu.be equivalent as a str. Expect that any such 
# URL will be in one of the formats below. Assume that the value of src 
# will be surrounded by double quotes. And assume that the input will 
# contain no more than one such URL. If the input does not contain any 
# such URL at all, return None.

import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        url_pattern = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if url_pattern:
            split_url = url_pattern.groups()
            return ("https://youtu.be/" + split_url[3])


if __name__ == "__main__":
    main()