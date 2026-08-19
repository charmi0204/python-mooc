# -*- coding: utf-8 -*-

import json
import os
import numpy as np





students = [
    "charmi patel",
    "tanu patel",
    "Rutu",
    "bansi patel",
    "riva",
    "ruhi Patel",
    "dhruvi",
    "diya",
    "deni",
    "janu"
]

file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "students.json"
)


data = {"students": students}

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("students.json created successfully!")




with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

students = data["students"]

print("Students loaded from JSON:")
print(students)


if len(students) != 10:
    print("Error: JSON must contain exactly 10 students.")
    raise SystemExit



batch = input("\nEnter Batch Name: ").strip()

if batch == "":
    print("Batch name cannot be empty.")
    raise SystemExit

department = batch.split("-")[-1].replace("_", " ")





subjects = (
    "Maths",
    "Physics",
    "Chemistry",
    "Programming",
    "English"
)




roll_numbers = range(1, 11)

print("\n==========================================")
print("ROLL NUMBER AND STUDENT NAME")
print("==========================================")

for roll, name in zip(roll_numbers, students):
    print("Roll No:", roll, "| Name:", name)


marks = []

print("\n==========================================")
print("ENTER MARKS")
print("==========================================")

for name in students:

    print("\nMarks for", name)

    student_marks = []

    for subject in subjects:

        while True:

            try:
                mark = float(
                    input("Enter " + subject + " marks (0-100): ")
                )

                if 0 <= mark <= 100:
                    student_marks.append(mark)
                    break

                print("Invalid! Marks must be between 0 and 100.")

            except ValueError:
                print("Invalid! Enter numbers only.")

    marks.append(student_marks)



marks = np.array(marks)

print("\nMarks Array:")
print(marks)



total = np.sum(marks, axis=1)

percentage = (total / 500) * 100


print("\n==========================================")
print("STUDENT PERFORMANCE")
print("==========================================")

for i in range(10):
    print(
        "Roll:", i + 1,
        "| Name:", students[i],
        "| Total:", total[i],
        "| Percentage:", round(percentage[i], 2), "%"
    )




subject_average = np.mean(marks, axis=0)

print("\n==========================================")
print("SUBJECT AVERAGES")
print("==========================================")

for i in range(5):
    print(
        subjects[i],
        ":",
        round(subject_average[i], 2)
    )



highest_mark = np.max(marks)
lowest_mark = np.min(marks)

print("\nHighest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)




highest_index = np.argmax(total)
lowest_index = np.argmin(total)

highest_student = students[highest_index]
lowest_student = students[lowest_index]

print("\nHighest Scoring Student:", highest_student)
print("Lowest Scoring Student:", lowest_student)



class_average = np.mean(percentage)

print(
    "\nClass Average Percentage:",
    round(class_average, 2),
    "%"
)




highest_subject = subjects[np.argmax(subject_average)]
lowest_subject = subjects[np.argmin(subject_average)]

print("Highest Average Subject:", highest_subject)
print("Lowest Average Subject:", lowest_subject)




print("\n==========================================")
print("FIRST 3 STUDENTS - LAST 2 SUBJECTS")
print("==========================================")

print(marks[:3, -2:])




print("\nAvailable Subjects:")

for subject in subjects:
    print("-", subject)

search_subject = input(
    "\nEnter subject to search: "
).strip()

if search_subject in subjects:
    print(
        search_subject,
        "found at index",
        subjects.index(search_subject)
    )
else:
    print("Subject not found.")





distinction = []

for i in range(10):
    if percentage[i] >= 85:
        distinction.append(students[i])

print("\n==========================================")
print("DISTINCTION STUDENTS")
print("==========================================")

print(distinction)




failed = []

for i in range(10):
    if np.any(marks[i] < 40):
        failed.append(students[i])

print("\n==========================================")
print("FAILED STUDENTS")
print("==========================================")

print(failed)




above_average = []

for i in range(10):
    if percentage[i] > class_average:
        above_average.append(students[i])

print("\n==========================================")
print("STUDENTS ABOVE CLASS AVERAGE")
print("==========================================")

print(above_average)




print("\nReversed Names:")
print(students[::-1])




print("\nAlphabetical Names:")
print(sorted(students))




print("\n")
print("=" * 60)
print("          ACADEMIC PERFORMANCE REPORT")
print("=" * 60)

print("Batch Name                :", batch)
print("Department Name           :", department)
print("Total Number of Students  :", len(students))
print("Class Average Percentage  :", round(class_average, 2), "%")
print("Highest Scoring Student   :", highest_student)
print("Lowest Scoring Student    :", lowest_student)
print("Subject with Highest Avg  :", highest_subject)
print("Subject with Lowest Avg   :", lowest_subject)
print("Number of Distinction     :", len(distinction))
print("Number of Failed Students :", len(failed))

print("=" * 60)
print("                  END OF REPORT")
print("=" * 60)