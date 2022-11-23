def word_counter():
    phrase = input("insert a phrase: ")
    l_phrase = phrase.split(" ")
    counter = 0
    for char in l_phrase:
        if char.isalpha():
            counter += 1
    print(f'the total number of words in your phrase is {counter}')
    print(l_phrase)


word_counter()
