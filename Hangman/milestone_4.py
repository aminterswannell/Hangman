import random
word_list = ['apple', 'manhattan', 'squeeze', 'pigeon', 'serious']
word = random.choice(word_list)

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ['_']
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.num_letters -= 1
            print(self.num_letters)
            for i, char in enumerate(self.word):
                if char == guess:
                    self.word_guessed[i] = char
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Unlucky! {guess} is not in the word.")
            print(f"You have {self.num_lives} left")
        

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter:")
            print(self.word_guessed)
            if guess.isalpha() == False or len(guess) != 1:
                print("invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
            print(self.check_guess(guess))
            

game_1 = Hangman(word_list)
game_1.ask_for_input()