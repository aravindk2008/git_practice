#!/usr/bin/env python3

with open ("my_diary.txt", "w") as f:
	f.write("Today I learned Python.\n")
	f.write("I completed my lab assignment.\n")
	f.write("I practiced Git commands.\n")
	f.write("I watched a football match.\n")
	f.write("I am preparing for exams.\n")
with open ("my_diary.txt", "r") as f:
	lines=f.readlines()

line_count=len(lines)

word_count = len(" ".join(lines).split())

print ("lines:",  line_count)
print ("words:",  word_count)
