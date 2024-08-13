# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:20:43 2024

@author: Student
"""

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
if a == 0 and b == 0:
    print("Phuong trinh co vo so nghiem.")
elif a == 0 and b != 0:
    print("Phuong trinh vo nghiem.")
else:
    print("Nghiem cua phuong trinh ",a,"x+",b," la: ", -b/a)
