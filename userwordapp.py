import random
import string

user_word = input("Enter a word: ")
user_option = input("What would you want to do: ")

def choose_option(user_option):
    match user_option:
        case "Count a random number":
            result = ran_letter_counter(user_word)
            return result
        case "Palindrone check":
            result = palin_chk(user_word)
            return result
        case "Count letters":
            return letter_count(user_word)
        case _:  
            print("Option not recognized")
            return None

def ran_letter_counter(word):
    letters = string.ascii_letters
    random_letter = random.choice(letters)
    letter_list = []
    icounter = 0

    for char in word:
        if char.lower() == random_letter.lower():
            letter_list.append(char)


    if len(letter_list) ==  1:
        print(f'There is {len(letter_list)} {random_letter} in {word}')
    else:
        print(f'There are {len(letter_list)} {random_letter}s  is in \'{word}\'')

    return print(f'letters = {letters}')

def palin_chk(word):
    is_palindrone = False
    if word == word[::-1]:
        is_palindrone = True
        print(f"The word {word} is a palindrone!")
    else:
        is_palindrone = False
        print(f"The word {word} is not a palindrone!")

def letter_count(word):
    word_letters = []
    for char in word:
        word_letters.append(char)
        print(char)
   
    if len(word_letters) > 1: 
        print(f"There are {len(word_letters)} letters in the word {word}.")
    else:
        print(f"There is one letter in the word {word}. Why did you even type this in?")

    

#def savetofile(word):

print(user_word)
print(user_option)
#print(word_letters)


choose_option(user_option)
