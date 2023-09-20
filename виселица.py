import random

def hangman():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word contains", len(word), "letters.")

    while attempts > 0:
        print("\nAttempts left:", attempts)
        letter = input("Guess a letter: ").lower()

        if len(letter) != 1:
            print("Please enter a single letter.")
            continue

        if letter in guessed_letters:
            print("You already guessed that letter.")
            continue

        if letter not in word:
            print("Incorrect guess!")
            attempts -= 1
        else:
            print("Correct guess!")

        guessed_letters.append(letter)

        word_progress = ""
        for char in word:
            if char in guessed_letters:
                word_progress += char
            else:
                word_progress += "_"

        print("Current progress:", word_progress)

        if "_" not in word_progress:
            print("\nCongratulations! You guessed the word:", word)
            return

    print("\nGame over! The word was:", word)

hangman()
