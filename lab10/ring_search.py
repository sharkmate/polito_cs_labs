"""
Write a program that searches for a given word in the contents of a group of files.
The program must ask the user for input:
I. A list of file names on a single line, separated by commas;
II. A word to search. File names must be stored in a list,
while the word to be searched must be stored in a variable.
The program must display all lines that contain the word,
even as a substring of other words,
without distinguishing between uppercase and lowercase letters.
Each displayed line must be preceded by the name of the
file in which it is located. For example, if the word to be searched is 'ring',
and the list contains the files:

"""


def main():

    user_input = input("insert file names separated by commas: ").replace(" ", "")
    word = input("insert a word to search: ")
    file_names = user_input.split(",")
    for name in file_names:
        try:
            with open(name) as file:
                lines = file.readlines()
                for line in lines:
                    if word in line.lower():
                        print(f"{name}: {line[0:line.find(word)]}({word}){line[line.find(word)+3:]}")
        except FileNotFoundError:
            print(f'ops "{name}" is not an existing directory you made a fucky wacky')



if __name__ == '__main__':
    main()


