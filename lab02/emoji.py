
""" 02.2.4 Emoji. According to data collected by the Unicode Consortium1
, the non-profit organization
responsible for digitizing the world's languages, "tears of joy" ( ) account for more than 5% of all
emojis used (the only other character that comes close to it is the ). The top ten emojis used
worldwide are: .
When exchanging messages on Telegram (or on your favorite messaging app), which are the three
emojis that you personally use most frequently? Using the Unicode encoding information collected
here2
, you can create a program that shows a scheme for each of these three emojis:
I. the position in the ranking (rank);
II. the Unicode Number;
III. the Unicode Name;
IV. the emoji itself.
Format the output so that the information related to each of the three emojis is collected on one
line, and the different fields are aligned vertically.
"""


import unicodedata


def main():
    emoji_1 = "💀"
    emoji_2 = "😭"
    emoji_3 = "🔥"

    # function ord() returns the unicode character encoding
    print(f"RANK  20  -  {ord(emoji_1):4X} - {unicodedata.name(emoji_1):30} - {emoji_1}")

    print(f"RANK  15  -  {ord(emoji_2):4X} - {unicodedata.name(emoji_2):30} - {emoji_2}")

    print(f"RANK  22  -  {ord(emoji_3):4X} - {unicodedata.name(emoji_3):30} - {emoji_3} ")


if __name__ == '__main__':
    main()
