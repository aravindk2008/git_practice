#!/usr/bin/env python3
def is_even(n):
    return n % 2 == 0

def count_evens(lst):
    count = 0

    for n in lst:
        if is_even(n):
            count += 1

    return count

numbers = [1,2,3,4,5,6,7,8,9,10]

print("Even count =", count_evens(numbers))
