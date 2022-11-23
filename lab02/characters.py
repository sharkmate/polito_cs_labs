"""
Write a program that stores a string in a variable and displays the first three
characters of the string, followed by three periods, again followed by the last three characters. For
example, if the string is initialized to the value "Mississippi", the program must display "Mis...
ppi". What happens to the string is shorter than 6 characters? What if it's shorter than 3
characters?
"""


def main():
    word = input("insert a word")
    print(f'{word[0:4]}...{word[-3:]}')


if __name__ == '__main__':
    main()
