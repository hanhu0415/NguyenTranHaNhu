# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
BÀI 1: PHƯƠNG TRÌNH BẬC 1
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
if a == 0 and b == 0:
    print("Phuong trinh co vo so nghiem.")
elif a == 0 and b != 0:
    print("Phuong trinh vo nghiem.")
else:
    print("Nghiem cua phuong trinh ",a,"x+",b," la: ", -b/a)
    
BÀI 2: PHƯƠNG TRÌNH BẬC 2
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
    
BÀI 3: KIỂM TRA BA CẠNH TAM GIÁC
a = float(input(" Nhap canh a: "))
b = float(input(" Nhap canh b: "))
c = float(input(" Nhap canh c: "))
if a+b>c and a+c>b and b+c>a:
    print("a, b, c la ba canh cua tam giac")
else:
    print("a, b, c khong la ba canh cua tam giac")
    
BÀI 4: KIỂM TRA TAM GIÁC ĐẶC BIỆT
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
    
BÀI 5: Điểm trung bình (GPA)
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
    
BÀI 6: Tính tiền taxi
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
    
BÀI 7: Kéo Búa Bao
import random

def keo_bua_bao():

  # Danh sách các lựa chọn
  lua_chon = ["kéo", "búa", "bao"]

  # Người chơi chọn
  nguoi_choi = input("Bạn chọn gì? (kéo/búa/bao): ").lower()

  # Máy tính chọn ngẫu nhiên
  may_tinh = random.choice(lua_chon)

  print(f"Bạn chọn: {nguoi_choi}")
  print(f"Máy tính chọn: {may_tinh}")

  # Quyết định thắng thua
  if nguoi_choi == may_tinh:
    print("Hòa!")
  elif (nguoi_choi == "kéo" and may_tinh == "bao") or \
       (nguoi_choi == "búa" and may_tinh == "kéo") or \
       (nguoi_choi == "bao" and may_tinh == "búa"):
    print("Bạn thắng!")
  else:
    print("Bạn thua!")

# Chạy chương trình
keo_bua_bao()
"""
distance = float(input("Nhap do dai doan duong den truong (m): "))
if distance > 1200:
    print("Duong den truong qua xa.")
else:
    print("Duong den truong gan.")
