# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:08:08 2024

@author: Student
"""

a = float(input(" Nhap canh a: "))
b = float(input(" Nhap canh b: "))
c = float(input(" Nhap canh c: "))
if a+b>c and a+c>b and b+c>a:
    print("a, b, c la ba canh cua tam giac")
else:
    print("a, b, c khong la ba canh cua tam giac")