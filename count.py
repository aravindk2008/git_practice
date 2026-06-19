#!/usr/bin/env python3

counts = {}

with open("text.txt", "r") as f:
    text = f.read()

words = text.split()

for word in words:
    word = word.lower().strip(".,!?;:\"'()")

    if word:
        counts[word] = counts.get(word, 0) + 1

top10 = sorted(counts.items(), key=lambda x: x[1],reverse=True)[:10]

print("Top 10 Most Common Words:\n")

for word, count in top10:
    print(word, ":", count)
