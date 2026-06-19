#!/usr/bin/env python3

numbers = []

while True:
    x = input("Enter number (done to stop): ")

    if x == "done":
        break

    try:
        numbers.append(float(x))
    except ValueError:
        print("Invalid input")

if numbers:
    print(f"Count:{len(numbers)} Min:{min(numbers)} Max:{max(numbers)}Sum:{sum(numbers)} Avg:{sum(numbers)/len(numbers)}")
else:
    print("No numbers entered")
