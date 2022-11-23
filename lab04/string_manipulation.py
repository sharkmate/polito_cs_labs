"""
Write a program that takes as an input a line of text as a string and outputs the following requests:

Only the capital letters in the string.
The letters in the string in even positions.
The same string with vowels (uppercase and lowercase) replaced by an underscore (_).
How many digits are contained in the string.
The positions of all vowels in the string.
"""

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


def main():
    def only_upper():
        upper_case = ""
        for i in phrase:
            if i.isupper():
                upper_case += i
        print(f" the upper case characters in your phrase are {upper_case}")

    def even_positions():
        even_char = ""
        for i in phrase[::2]:
            even_char += i
        print(f"the characters in an even positions are {even_char}")

    def no_vowels():

        new_phrase = phrase
        for i in phrase:
            if i in vowels:
                new_phrase = new_phrase.replace(i, "_")
        print(f" your new phrase without vowels is {new_phrase}")

    def count_digits():
        count = 0
        for i in phrase:
            if i != " ":
                count += 1
        print(f"the total number of digits in your phrase is {count}")

    def point_vowel():
        vowel_index = ""
        for i in phrase:
            if i in vowels:
                vowel_index += str(phrase.find(i))
        print(f"your vowels are located at the positions {vowel_index}")

    only_upper()
    even_positions()
    no_vowels()
    count_digits()
    point_vowel()


if __name__ == "__main__":
    main()
