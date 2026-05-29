import random
words = ["apple", "tiger", "house", "chair", "water"]
secret_word = random.choice(words)
guessed_letters = []
attempts = 6
print("Welcome to Hangman!")
while attempts > 0:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)
    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break
    print("Incorrect guesses left:", attempts)
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in secret_word:
        print("Correct guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        guessed_letters.append(guess)
        attempts -= 1
if attempts == 0:
    print("\nYou lost!")
    print("The word was:", secret_word)
