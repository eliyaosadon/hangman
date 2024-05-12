import functionality
from functionality import check_win, show_hidden_word, check_valid_input, try_update_letter_guessed, choose_word

MAX_TRIES = 6
old_letters_guessed = []
MISTAKES = 0


def play_game(chosen_word):
    global MISTAKES
    MISTAKES = 0  # restart the hangman positions
    while MISTAKES <= MAX_TRIES:
        # prints the hangman stage in 'mistakes+1'
        functionality.print_hangman(MISTAKES + 1)
        print(functionality.show_hidden_word(chosen_word, old_letters_guessed))
        # checks if the guess is valid
        letter_guessed = check_validation()
        # checks if the letter is in the chosen word
        is_exist = try_update_letter_guessed(letter_guessed, old_letters_guessed, chosen_word)
        # adds the letter to all the guesses the player had
        old_letters_guessed.append(letter_guessed.lower())
        # if the letter doesn't exist in the word
        if not is_exist:
            MISTAKES += 1
            print(" ): ")
            # checks if he won
        if check_win(chosen_word, old_letters_guessed):
            return True
    return False


# this function checks the validation of the input - if not valid
# presents all the last guesses and ask him to guess again
def check_validation():
    letter_guessed = input("Enter your guess : ")
    while not (check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed_str = ' -> '.join(sorted(old_letters_guessed))
        print("X\n" + old_letters_guessed_str)
        letter_guessed = input("Enter your guess : ")

    return letter_guessed


def main():
    # Print the welcome screen
    functionality.welcom_page(MAX_TRIES)
    file_path = input("Enter file path: ")
    play_again = 1
    global old_letters_guessed
    while play_again == 1:
        old_letters_guessed = []
        index = int(input("Enter index: "))
        chosen_word = functionality.choose_word(file_path, index)
        print("Let's start!\n")
        if play_game(chosen_word):
            print("WIN!")
        else:
            print("LOSE, TRY AGAIN")
        play_again = int(input("if you want to play again press 1\notherwise, 0 : "))  # manu for 'play again' or quit


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()