"""
Write a program that reads a string and displays the appropriate messages, after checking if:

it contains only letters
it contains only capital letters
it contains only lowercase letters
it contains only digits
it contains only letters and digits
it starts with a lowercase letter
it ends with a point
"""



def main():
    phrase = input("insert a phrase")
    if phrase.isupper():
        print("your phrase only contains capital letters")
    elif phrase.islower():
        print("your phrase only contains lowercase letters")
    if phrase.isnumeric():
        print("your phrase is only digits")
    elif phrase.isalnum():
        print("your phrase only contains digits and letters")
    if phrase[0].isupper():
        print("your phrase starts with a capital letter")
    elif phrase[0].islower():
        print("your phrase starts with a lowercase letter")
    if phrase[-1] == ".":
        print("your phrase ends with a point")
    else:
        print("you sure this is even a phrase man?")


if __name__ == "__main__":
    main()
