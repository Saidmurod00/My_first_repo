# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 06:50:54 2024

@author: Saidmurod00
"""
def fresh(sabzavot, meva, ziravor=''):
    """Fresh tayorlash uchun kerakli mahsulotlar kiritiladi 
    sabzavot va meva kiritish zarur ziravor ixtiyoriy"""
    if ziravor:
        fresh_tayorlash = f"{sabzavot} {meva} {ziravor}"
    else:
        fresh_tayorlash = f"{sabzavot} {meva}"
    return fresh_tayorlash

fresh_1 = fresh("sabzi", "qovoq")
fresh_2 = fresh("sabzi", "olma", "rayxon")
print(f"menudagi yangi freshlar {fresh_1}, va {fresh_2}")