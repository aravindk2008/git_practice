#!/usr/bin/env python3
import json

def add_student(records, name, roll, gpa):
    records.append({
        "name": name,
        "roll": roll,
        "gpa": gpa
    })

def find_by_roll(records, roll):
    for student in records:
        if student["roll"] == roll:
            return student
    return None

def delete_student(records, roll):
    for student in records:
        if student["roll"] == roll:
            records.remove(student)
            return True
    return False

def print_all_sorted_by_gpa(records):
    for student in sorted(records, key=lambda x: x["gpa"], reverse=True):
        print(student)
def save_records(records, filename):
    with open(filename, "w") as f:
        json.dump(records, f, indent=2)

def load_records(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def main():

    records = load_records("students.json")

    add_student(records, "vic", "11", 8.5)
    add_student(records, "rock", "12", 9.2)
    add_student(records, "Alex", "13", 7.8)

    print("Find Roll 12:")
    print(find_by_roll(records, "12"))

    print("\nSorted by GPA:")
    print_all_sorted_by_gpa(records)

    delete_student(records, "13")

    save_records(records, "students.json")

    print("\nRecords saved to students.json")

if __name__ == "__main__":
    main()
