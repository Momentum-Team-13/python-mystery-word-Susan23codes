import random

guessed_letters = []
guess_count = 8


def ask_to_play_game():
    read_file = open_and_read_file()
    word_to_guess = get_random_word(read_file)
    opening_input_question = input(
        "Would you like to play a mystery word game?  Y/N ")
    if opening_input_question in ["Y",  "y"]:
        print(
            f"Great!  Let's begin! Your word is {len(word_to_guess)} letters long.  Here are your word blanks.")
        blanks = splitting_word_into_letter_array_and_blanks(word_to_guess)
        blanks = guessing_letters(blanks, word_to_guess)
    elif opening_input_question in ["N", "n"]:
        print("Okay, bye!")
    else:
        print("That's not a valid answer")


def open_and_read_file():
    text_file = "words.txt"
    with open(text_file) as open_file:
        text = open_file.read()
    word_list = text.split()
    return word_list


def get_random_word(word_list):
    random_word = random.choice(word_list)
    # print(random_word)
    return random_word


def splitting_word_into_letter_array_and_blanks(word_to_guess):
    letter_array = list(word_to_guess)
    blanks = (len(word_to_guess) * "_")
    print(blanks)
    return blanks


def guessing_letters(blanks, word_to_guess):
    print(f'Here are your guessed letters so far: {guessed_letters}')
    guessed_letter = input("Choose a letter: ")
    letter_array = list(word_to_guess)
    global guess_count
    while ("_") in blanks:
        if guessed_letter in guessed_letters:
            print("You've already guessed that letter!  Guess again.")
            guessing_letters(blanks, word_to_guess)

        for index, letter in enumerate(letter_array):
            if letter == guessed_letter:
                blanks = blanks[:index] + \
                    guessed_letter.upper() + blanks[index+1:]
                print(f'{blanks} \nGreat guess!  Now guess another letter!')

        if guessed_letter not in word_to_guess:
            guess_count -= 1
            print(
                f"Sorry, that letter isn't there! You have {guess_count} guesses remaining!\n{blanks}")

        if guess_count == 0:
            print(
                f"Sorry, you're out of guesses!  The mystery word was: {word_to_guess.upper()}")
            exit()

        elif "_" not in blanks:
            break

        else:
            guessed_letters.append(guessed_letter)
            return guessing_letters(blanks, word_to_guess)
    print(f'Great job! You win! The mystery word was {word_to_guess.upper()}')


if __name__ == "__main__":
    ask_to_play_game()
