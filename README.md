# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. 
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

The aim of this project was to utilise the Python skills I have picked up so far on the course, in order to make a working version of the game Hangman, for the user to play against the computer, with the computer selecting randomly from a pre-determined list of words.
The game is made by creating a class 'Hangman', and a separate 'play_game' function which is used to call an instance of the Hangman function and run the necessary logic to be able to play the game smoothly. 

In completing this project I learned the necessity of clear, non-repetitive code, and the importance of checking how a code runs, as I ran into issues with while loops running infinitely without breaking. 

## Installation Instructions:
Download the milestone_5.py file from the Hangman folder of this repository, and run on your local machine in order to play the game.

## Usage Instructions:
In order to play the game, you must guess a single alphabetical character when prompted, guessing anything other than a single alphabetical character will cause the program to ask you to re-try and enter again. 
You have 5 lives, each incorrect guess loses you a life, run out of lives and you lose the game.
You must guess until you have gotten the entire word correctly, which will be clear as the list of '_' corresponding to the letters in the word will now just read the word in single characters, and the number of unique letters left to guess will show as 0.

## File Structure:
The file first imports the random module, to be used in randomly selecting a word to be guessed by the user.
It then defines the variables 'word_list', which is a list of words to be randomly selected from by the computer, and 'word' which is the word selected from 'word_list'.
The 'Hangman' class is created, taking self, word_list and num_lives as parameters. 

Inside the class' initialiser function, the following parameters are defined:

'word_list' is the list of words the computer will select from.
'num_lives' is the number of lives remaining for the player before they are out of guesses, pre-set to 5 in this instance.
'word' is the word selected randomly by the computer from word_list using the imported Python random module.
'word_guessed' is a list of '_' that is updated whenever the player makes a correct guess, to replace one or more of the '_' with the guess, in the correct position, corresponding to that letters position within the word. For example if the word was 'apple' and the user guessed 'a' as their first guess, the list would be updated from ['_', '_', '_', '_', '_'] to ['a', '_', '_', '_', '_'].
'num_letters' is the number of unique letters contained in the word selected by the computer, each time a correct guess is made the length of this list is updated by - 1, when the number of unique letters left to guess hits 0, the user has won the game.
'list_of_guesses' is an empty list, which is updated with each guess the user makes.

The function 'check_guess' is defined, taking self and the variable 'guess' which corresponds to the users input, as parameters.
The function checks whether the users guessed letter is in the word selected by the computer, and if it is, prints 'Good guess! {guess} is in the word' and updates the value of num_letters by - 1. If the guess is not part of the word, prints 'Unlucky! {guess} is not part of the word.' , updates the value of num_lives by - 1, and prints 'You have {num_lives} remaining.'

The function 'ask_for_input' is defined, taking self as a parameter. 
This function uses a while loop to iteratively check whether the users input is in the correct format, whether it has already been guessed, and to append the list_of_guesses variable with the users guess. If the users input is not a single alphabetical character, the function prints 'Invalid letter. Please enter a single alphabetical character.'. If the user inputs a single alphabetical character, but one they have input already, prints 'You already tried that letter!'. If all criteria are met by the users input, the guess is appended to list_of_guesses, and checked by the 'check_guess' function.

For the final logic of the game, a function is defined outside of the Hangman class.
The 'play_game' function contains a while loop, to check whether the num_lives remaining for the user is equal to 0, and if it is, print 'You lost!'. The function also checks whether the num_letters variable is > 0, as this means the player still has letters left to guess to complete the word, if the variable is > 0, the function calls for the ask_for_input function to continue the computer asking the user for guesses. Finally, the function checks whether the num_lives > 0 and the num_letters = 0, as if this is the case then the user has successfully guessed all of the letters, without running out of lives, therefore winning the game, as such the function prints 'Congratulations! You\'ve won!'.

## License Information:
An MIT License has been used for this project.
