# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:28:55 2026

@author: charmi04
"""




marks = []
students = {}


for i in range(10):
    print("\nStudent", i + 1)
    name = input("Enter Name: ")
    mark = int(input("Enter Marks: "))

    marks.append(mark)
    students[name] = mark


marks_tuple = tuple(marks)


highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)


unique_marks = set(marks)


print("\n===== Student Marks Analysis =====")
print("Marks List :", marks)
print("Marks Tuple :", marks_tuple)
print("Student Dictionary :", students)

print("\nHighest Marks :", highest)
print("Lowest Marks :", lowest)
print("Average Marks :", round(average, 2))

print("\nStudents Scoring Above Average:")
for name, mark in students.items():
    if mark > average:
        print(name, ":", mark)

print("\nUnique Marks (After Removing Duplicates):")
print(unique_marks)