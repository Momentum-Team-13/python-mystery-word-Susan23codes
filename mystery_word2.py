mystery_word = "hello"
letter_array = list(mystery_word)
# print(word_array)
blanks = len(letter_array) * "_"
# print(blanks) 
blanks_array = list(blanks)
print(blanks_array)
letter_guessed = ""

user_guess = input("Make your first guess! ")
    # print(letter_array)
if user_guess not in letter_array:
        print("Sorry, that letter is not in the word!  Please guess again!")

for index, letter in enumerate(letter_array):
    if letter == user_guess:
        blanks_array[index] = user_guess
        # print(blanks_array)
        word = (" ").join(blanks_array)
        print("Great guess!  Guess another letter!")
        print(word.upper())

#It doesn't loop yet for multiple guesses but bare-bones code for guessing