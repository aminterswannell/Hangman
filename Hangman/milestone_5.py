import random
word_list = ['apple', 'manhattan', 'squeeze', 'pigeon', 'serious']
word = random.choice(word_list)

class Hangman:
    """
    This class is used to build the user input game: Hangman.

    Attributes:
    word_list: the list of words for the computer to randomly select from
    num_lives: the number of lives the user has left before they lose the game
    word: the word randomly selected by the computer from word_list
    word_guessed: list of '_' to represent the letters of the word to be guessed
    num_letters: the number of letters left to be guessed by the user
    list_of_guessed: a list of all the guesses made by the user
    """
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ['_']
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        This function is used to check whether the guess made by the user is part of the word selected by the computer.

        If guess is correct, updates the value of num_letters by - 1, 
        prints to tell the user their guess was successful, 
        appends the word_guessed list with the users guess, 
        in the correct place corresponding to the letters place in the word.

        If guess is incorrect, updates value of num_lives by - 1,
        prints to tell the user their guess was unsuccessful,
        prints to tell the user how many lives they have remaining.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            self.num_letters -= 1
            print(self.num_letters)
            for i, char in enumerate(self.word):
                if char == guess:
                    self.word_guessed[i] = char
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f'Unlucky! {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left')
        

    def ask_for_input(self):
        """
        This function is used to ask the user to input a guess, and check its validity.

        If the user does not input a single alphabetical character, 
        function prints to request the user guesses again using this criteria, breaks loop.

        If the user inputs a single alphabetical character they have guessed before,
        function prints to remind user they have already input that letter, breaks loop.

        If the user inputs a single alphabetical character they have not input before,
        function appends this letter to the list_of_guesses,
        runs the check_guess function to check if the letter is part of the word, breaks loop.
        """
        while True:
            guess = input('Guess a letter:')
            print(self.word_guessed)
            if guess.isalpha() == False or len(guess) != 1:
                print('Invalid letter. Please enter a single alphabetical character.')
                break
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
                break
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break
    
def play_game(word_list):
    """
    This function is used for the user to play the game.

    Defines a set number of lives for the user to start with, and an instance of the class 'Hangman'.

    The function uses a while loop.
    Inside the while loop, checks whether the users number of lives remaining is equal to 0,
    prints 'You lost!' if it is.
    Checks whether the num_letters is > 0,
    calls the ask_for_input function if it is as the user needs to keep inputting guesses.
    Checks whether the num_lives > 0 and num_letters = 0,
    if it is then the user has won the game,
    prints to congratulate them, and breaks out of the loop.

    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
             game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters == 0:
            print('Congratulations! You\'ve won!')
            break

if __name__ == "__main__":         
   game_1 = Hangman(word_list)
   play_game(word_list)

