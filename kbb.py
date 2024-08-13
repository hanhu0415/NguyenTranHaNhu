# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:30:55 2024

@author: DELL
"""
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
