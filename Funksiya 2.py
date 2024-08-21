# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 10:53:55 2024

@author: Saidmurod00
"""
#parametr berib bajarilgan funksiyalar
def salom_ber(ism):
    """Foydalanuvchining ismini so'rab,
    unga salom beruvchi funksiya"""
    print(f"Assalomu aleykum, hurmatli {ism.title()}!")
    
salom_ber("saidmurod")
salom_ber("olim")

def yoshini_ayt(yosh):
    """Kiritilgan yoshini aytadi"""
    print(f"Foydalanuvchilarning yoshi {yosh}")
    
yoshini_ayt("o'rta yoshda")

def dasturlash_tili(dastur):
    """foydalanuvchi qaysi dasturlash tilidan 
    foydalanadi"""
    print(f"Foydalanuvchi {dastur}-dan foydalanadi")
    
dasturlash_tili("Python")

