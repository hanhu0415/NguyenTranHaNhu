# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 09:03:40 2024

@author: DELL

"""

a=float(input("Nhap canh a: "))
b=float(input("Nhap canh b: "))
c=float(input("Nhap canh b: "))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("a,b,c tao thanh tam giac deu.")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("a,b,c, tao thanh tam giac can.")
    elif (a*a)+(b*b)==c*c or (a*a)+(c*c)==b*b or (c*c)+(b*b)==a*a:
        print("a,b,c tao thanh tam giac vuong.")
    else: 
        print("a,b,c tao thanh tam giac thuong.")
else:
    print("a, b, c khong la ba canh cua tam giac")