# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""





roll_no = int(input("Enter Roll No: "))
name = input("Enter Name: ")
age = int(input("Enter Age: "))

m1 = float(input("Enter Marks of Subject 1: "))
m2 = float(input("Enter Marks of Subject 2: "))
m3 = float(input("Enter Marks of Subject 3: "))


total = m1 + m2 + m3
percentage = total / 3


if m1 >= 40 and m2 >= 40 and m3 >= 40:
    result = "PASS"
else:
    result = "FAIL"



print(f"Roll No    : {roll_no}")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"Marks      : {m1}, {m2}, {m3}")
print(f"Total      : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Result     : {result}")