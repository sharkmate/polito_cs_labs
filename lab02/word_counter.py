# counts number of words in a phrase

def word_counter():
    phrase = input("insert a phrase: ")
    space_counter = 1
    for char in phrase:
        if char == " ":
            space_counter += 1
    print(f'the total number of words in your phrase is {space_counter}')


word_counter()
