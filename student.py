#!/usr/bin/env python3
import json

# Files
STUDENTS_FILE = "students.json"
SUBJECTS_FILE = "subjects.json"
MARKS_FILE = "marks.json"


def load_data(filename, default):
    try:
        with open(filename, "r") as f:
            data = json.load(f)

            if type(data) != type(default):
                return default

            return data
    except:
        return default




def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


students = load_data(STUDENTS_FILE, {})
subjects = load_data(SUBJECTS_FILE, [])
marks = load_data(MARKS_FILE, {})


def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    students[roll] = name
    print("Student added.")



def search_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Name:", students[roll])
    else:
        print("Student not found.")



def delete_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        del students[roll]
        print("Student deleted.")
    else:
        print("Student not found.")



def add_subject():
    subject = input("Enter Subject Name: ")

    if subject not in subjects:
        subjects.append(subject)
        print("Subject added.")
    else:
        print("Subject already exists.")



def add_marks():
    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Student not found.")
        return

    subject = input("Enter Subject: ")

    if subject not in subjects:
        print("Subject not found.")
        return

    try:
        mark = int(input("Enter Marks (0-100): "))

        if mark < 0 or mark > 100:
            print("Invalid marks.")
            return

        key = roll + "_" + subject
        marks[key] = mark

        print("Marks saved.")

    except:
        print("Enter valid number.")


def report_card():
    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Student not found.")
        return

    print("\n=REPORT CARD")
    print("Roll:", roll)
    print("Name:", students[roll])

    total = 0
    count = 0

    for subject in subjects:
        key = roll + "_" + subject

        if key in marks:
            mark = marks[key]
            grade = get_grade(mark)

            print(subject, "-", mark, "-", grade)

            total += mark
            count += 1
        else:
            print(subject, "- No Marks")

    if count > 0:
        average = total / count
        print("Average:", round(average, 2))
        print("Overall Grade:", get_grade(average))



def export_report():
    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Student not found.")
        return

    filename = roll + "_report.txt"

    with open(filename, "w") as f:
        f.write("REPORT CARD\n")
        f.write(f"Roll: {roll}\n")
        f.write(f"Name: {students[roll]}\n\n")

        total = 0
        count = 0

        for subject in subjects:
            key = roll + "_" + subject

            if key in marks:
                mark = marks[key]
                grade = get_grade(mark)

                f.write(f"{subject}: {mark} ({grade})\n")

                total += mark
                count += 1

        if count > 0:
            average = total / count
            f.write(f"\nAverage: {average:.2f}\n")
            f.write(f"Overall Grade: {get_grade(average)}\n")

    print("Report exported to", filename)



while True:
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Add Subject")
    print("5. Add Marks")
    print("6. Generate Report Card")
    print("7. Export Report")
    print("8. Save & Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        add_subject()

    elif choice == "5":
        add_marks()

    elif choice == "6":
        report_card()

    elif choice == "7":
        export_report()

    elif choice == "8":
        save_data(STUDENTS_FILE, students)
        save_data(SUBJECTS_FILE, subjects)
        save_data(MARKS_FILE, marks)

        print("Data saved. Goodbye!")
        break

    else:
        print("Invalid choice.")

