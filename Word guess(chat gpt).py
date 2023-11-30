import random

def play_game():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grapefruit", "honeydew"]
    word = random.choice(words)
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    print("Guess the letters to complete the word.")
    print("You have {} tries.".format(tries))

    while tries > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_word)

        if "_" not in display_word:
            print("Congratulations! You guessed the word '{}'!".format(word))
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print("Incorrect guess. {} tries remaining.".format(tries))
            if tries == 0:
                print("Game over! The word was '{}'.".format(word))
        else:
            print("Correct guess!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing!")

play_game()
