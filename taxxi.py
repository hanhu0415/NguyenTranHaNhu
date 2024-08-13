# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:11:19 2024

@author: DELL
"""

d=float(input("Ban muon di bao xa (km): "))
if d<=1:
    print("Tien taxi cua ban la: 20000")
elif d>1 and d<4:
    print("Tien taxi cua ban la: ", d*13000)
elif d>=4 and d<=8:
    print("Tien taxi cua ban la: ", (3*13000)+((d-3)*12000))
elif d>8 and d<=8.1:
    print("Tien taxi cua ban la: ", (3*13000)+(5*12000)+((d-8)*10000))
else:
    print("Tien taxi cua bn la: ", ((3*13000)+(5*12000)+(d-8)*10000)*0.92)
