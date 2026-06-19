#!/usr/bin/env python3
questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": 1
    },
    {
        "question": "Which language is used for scripting?",
        "options": ["Python", "HTML", "JPEG", "PNG"],
        "answer": 0
    },
    {
        "question": "How many days are there in a week?",
        "options": ["5", "6", "7", "8"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": 1
    },
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Chennai", "Delhi", "Kolkata"],
        "answer": 2
    }
]

score = 0

for q in questions:

    print("\n" + q["question"])

    for i, option in enumerate(q["options"], start=1):
        print(i, ".", option)

    answer = int(input("Enter your answer (1-4): "))

    if answer - 1 == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

percentage = (score / len(questions)) * 100

print("\nScore:", score, "/", len(questions))
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good Job!")
elif percentage >= 40:
    print("Average Performance")
else: 
    print("bad perrfromance")
