from random import choice
WORD_LIST = ["dog", "cat", "school", "house", "math", "learn"]
LIVE = 6

# get random word
word = choice(WORD_LIST)
# mske "_" list for each letter of word
word_list = ["_" for i in word]
# get input from the user

while True:
    usr_input = input("Letter: ")

    if usr_input in word:
        index = word.index(usr_input)
        word_list[index] = usr_input
        print(word_list)
    else:
        print("not in word")

