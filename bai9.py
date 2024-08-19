# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:43:59 2024

@author: Student
math.sqrt(a)-math.sqrt(b)
math.sqrt(math.sqrt(a))
math.sqrt(math.sqrt(b))
"""

import math
a=float(input("Nhap so thuc a: "))
b=float(input("Nhap so thuc b: "))
a1=math.sqrt(a)
b1=math.sqrt(b)
a2=math.sqrt(math.sqrt(a))
b2=math.sqrt(math.sqrt(b))
ab=math.sqrt(math.sqrt(a*b))
print("Gia tri cua bieu thuc la: ", ((a1-b1)/(a2-b2))-((a1+ab)/(a2+b2)))