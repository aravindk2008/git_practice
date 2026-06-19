#!/usr/bin/env python3
profile = {
    "name": "shaaaa",
    "roll_number": "2104244444",
    "branch": "ECE",
    "semester": 2,
    "gpa": 8.5,
    "city": "Chennai"
}
for key, value in profile.items():
    print(f"{key}: {value}")

profile["gpa"] = 9.0

profile["hobbies"] = ["Cricket", "Coding", "Music"]

if "email" in profile:
    print("Email exists")
else:
    print("Email does not exist")

print("\nUpdated Profile:")
for key, value in profile.items():
    print(f"{key}: {value}")
