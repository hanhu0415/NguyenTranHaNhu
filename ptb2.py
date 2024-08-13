# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
a=float(input("Nhap a: "))
b=float(input("Nhap b: "))
c=float(input("Nhap c: "))
if a==0 and b==0:
    print("Phuowng trinh vo nghiem!")
elif a==0 and b!=0:
    print("Phuong trinh co mot nghiem duy nhat x = ", -c/b)
elif a!=0 and b*b-(4*a*c)<0:
    print("Phuong trinh vo nghiem!")
elif a!=0 and b*b-(4*a*c)==0:
    print("Phuong trinh co mot nghiem kep x1=x2=", -b/(2*a))
elif a!=0 and b*b-(4*a*c)>0:
    print("Phuong trinh co hai nghiem phan biet: ")
    print("x1= ",(-b+math.sqrt(b*b-(4*a*c)))/(2*a))
    print("x2= ",(-b-math.sqrt(b*b-(4*a*c)))/(2*a))
else:
    print("Khong hop le!")