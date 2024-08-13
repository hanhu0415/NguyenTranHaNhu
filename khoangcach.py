# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:42:07 2024

@author: Student
"""

distance = float(input("Nhap do dai doan duong den truong (m): "))
if distance < 300:
    print("Duong den truong qua gan. Thoai, di bo.")
elif distance > 1200:
    print("Duong den truong xa qua. Thoai, di xe may.")
elif distance >= 300 and distance <= 700:
    print("Duong khong xa. Di xe dap ha.")
else:
    print("Khong xac dinh.")