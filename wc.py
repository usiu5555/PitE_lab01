import argparse

parser = argparse.ArgumentParser()
parser.add_argument("FILE", help="file that is analyzed")
parser.add_argument("-l", "--lines", help="print the newline counts", action="store_true")
parser.add_argument("-w", "--words", help="print the word counts", action="store_true")
parser.add_argument("-c", "--chars", help="print the character counts", action="store_true")
args = parser.parse_args()

f = open(args.FILE, "r")
lines_count = 0
words_count = 0
chars_count = 0
if args.lines or args.chars or args.words :
    while True:
        lines = f.readlines(1000)
        lines_count += len(lines)
        if args.words:
            for word in lines:
                words_count += len(word.split())
                if args.chars:
                    chars_count += len(word)
        if len(lines) == 0:
            break

echo = ""
if args.lines:
    echo += " " + str(lines_count)
if args.words:
    echo += " " + str(words_count)
if args.chars:
    echo += " " + str(chars_count)
print(echo[1:])