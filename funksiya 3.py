# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 06:17:57 2024

@author: Saidmurod00
"""
def mahsulotlar_jamlash(sabzavot, meva):
    """Bu yerda bazi mahsulotlarni korishingiz mumkun"""
    mahsulotlar_1 = f"{sabzavot} {meva}"
    return mahsulotlar_1    
sabzavot_meva = mahsulotlar_jamlash("sabzi", "olma")

print(f"Fresh qlish uchun eng yaxshi sabzavot va meva bu \
      {sabzavot_meva.title()} ")
      

def mahsulotlar_jamlash2(sabzavot, meva):
    """fresh qlish uchun eng yaxshi maaxsulotlar"""
    mahsulot = f"{sabzavot} {meva}"
    return mahsulot

mahsulotlar_1 = mahsulotlar_jamlash2("sabzi", "olma")
fresh_b = mahsulotlar_jamlash2("olma", "qovoq")

print(f"menuda 2 turdagi mahsulot bor 1-{mahsulotlar_1} 2-{fresh_b}")


def toliq_ism_yasa(ism, familiya):
    """Toliq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism
talaba = toliq_ism_yasa("saidurod", "mamasharipov")

print(talaba.title()) 