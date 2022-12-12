"""
 Enola Gay.
 Write a program that reads the text file input.txt,
and writes each line read in the file output.txt preceded
by its line number inserted as a comment between characters '/*' and ' */'.
"""


def main():

    try:
        with open("enola.txt") as text:
            lines = text.readlines()
    except FileNotFoundError:
        print("the file wasn't found")
        exit(0)

    for index, text in enumerate(lines):
        print(f"/*{index+1}*/{text}", end="")


if __name__ == '__main__':
    main()