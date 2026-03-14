user_word = input("Enter a word: ")
user_option = input("What would you want to do: ")

def choose_option(user_option):
    match user_option:
        case "Count":
            result = ran_letter_counter(user_word)
            return result


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
