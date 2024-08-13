# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:03:28 2024

@author: Student
"""

gpa = float(input("Nhap diem trung binh: "))
if gpa < 3.5:
    print("Hoc luc Kem.")
elif gpa >= 3.5 and gpa < 5:
    print("Hoc luc Yeu.")
elif gpa >= 5 and gpa < 7:
    print("Hoc luc Trung binh.")
elif gpa >= 7 and gpa < 8:
    print("Hoc luc Kha.")
elif gpa >= 8 and gpa < 9:
    print("Hoc luc Gioi.")
elif gpa >= 9 and gpa <= 10:
     print("Hoc luc Xuat sac.")
else:
    print("Diem khong hop le.")