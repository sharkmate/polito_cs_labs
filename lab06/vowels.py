# counts vowels in a word

word = input('insert a word')


def count_vowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_word = ""
    for char in word:
        if char in vowels:
            vowels_in_word += char
    print(f'you word contains a total of {len(vowels_in_word)} vowels which are {vowels_in_word}')


count_vowels()
