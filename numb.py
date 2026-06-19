#!/usr/bin/env python3
while True:
    try:
        n = int(input("Enter a number between 1 and 10: "))

        if 1 <= n <= 10:
            print(f"Great! You entered {n}.")
            break
        else:
            print("Must be 1 to 10.")

    except ValueError:
        print("Please enter a number.")
