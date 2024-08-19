# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:18:06 2024

@author: Student
"""

nam_sinh=int(input("Nhap nam sinh cua ban: "))
if 0<nam_sinh<2024:
    print("ban sinh nam ",nam_sinh,". Vay ban",2024-nam_sinh," tuoi.")
else:
    print("Nhap nam sinh hop le coi!")