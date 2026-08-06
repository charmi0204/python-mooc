# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 16:24:58 2026

@author: charmi04
"""



students = []
subjects = ["DS", "JAVA", "OS", "MONGODB", "CYBER SECURITY"]

for i in range(10):
    print(f"\nEnter Details of Student {i+1}")

    
    while True:
        try:
            roll = int(input("Roll No: "))
            if roll > 0:
                break
            else:
                print("Roll Number must be positive.")
        except ValueError:
            print("Invalid Input! Enter numeric Roll Number only.")

   
    while True:
        name = input("Name: ").strip()
        if name.replace(" ", "").isalpha():
            break
        else:
            print("Invalid Name! Name should contain only alphabets.")

    
    marks = []
    for sub in subjects:
        while True:
            try:
                mark = int(input(f"{sub} Marks: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid Marks! Enter marks between 0 and 100.")
            except ValueError:
                print("Invalid Input! Please enter numeric marks only.")

    total = sum(marks)
    per = total / len(subjects)

   
    if per >= 90:
        grade = "A"
    elif per >= 75:
        grade = "B"
    elif per >= 60:
        grade = "C"
    elif per >= 40:
        grade = "D"
    else:
        grade = "F"

    students.append({
        "Roll": roll,
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Per": per,
        "Grade": grade
    })


avg = sum(s["Per"] for s in students) / len(students)
print("\nClass Average =", round(avg, 2))


high = max(s["Total"] for s in students)
print("\nHighest Scorer(s):")
for s in students:
    if s["Total"] == high:
        print(s["Name"], "-", s["Total"])


low = min(s["Total"] for s in students)
print("\nLowest Scorer(s):")
for s in students:
    if s["Total"] == low:
        print(s["Name"], "-", s["Total"])


print("\nStudents Above Class Average:")
for s in students:
    if s["Per"] > avg:
        print(s["Name"])


print("\nStudents Failed in One or More Subjects:")
failed = False
for s in students:
    if any(m < 40 for m in s["Marks"]):
        print(s["Name"])
        failed = True

if not failed:
    print("None")


grade_dict = {}
for s in students:
    grade_dict.setdefault(s["Grade"], []).append(s["Name"])

print("\nGrade Dictionary:")
print(grade_dict)


print("\nNames in Alphabetical Order:")
for name in sorted([s["Name"] for s in students]):
    print(name)


first = second = -1

for s in students:
    if s["Total"] > first:
        second = first
        first = s["Total"]
    elif first > s["Total"] > second:
        second = s["Total"]

print("\nSecond Highest Scorer:")
for s in students:
    if s["Total"] == second:
        print(s["Name"], "-", s["Total"])


subject_avg = []

for i in range(len(subjects)):
    avg_marks = sum(s["Marks"][i] for s in students) / len(students)
    subject_avg.append(avg_marks)

print("\nSubject Averages:")
for i in range(len(subjects)):
    print(subjects[i], "=", round(subject_avg[i], 2))

print("\nSubject with Highest Average:",
      subjects[subject_avg.index(max(subject_avg))])



names = [s["Name"] for s in students]
duplicates = [n for n in set(names) if names.count(n) > 1]

print("\nDuplicate Names:")
if duplicates:
    print(duplicates)
else:
    print("None")

print("\nUnique Names:")
print(list(dict.fromkeys(names)))