#!/usr/bin/env python3

import random

best_score = None

while True:

    print("numbergame")

    if best_score is not None:
        print("Best Score:", best_score, "guesses")

    secret = random.randint(1, 100)
    guesses = 0

    while True:

        try:
            guess = int(input("Enter a guess (1-100): "))
            guesses += 1

            if guess < secret:
                print("Too low")

            elif guess > secret:
                print("Too high")

            else:
                print(f"Correct! {guesses} guesses.")

                if best_score is None or guesses < best_score:
                    best_score = guesses

                break

        except ValueError:
            print("Please enter a valid number.")

    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        break
