# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 09:51:08 2024

@author: @Saidmurod00
"""
menu = []

print("Menuni to'ldiramz")
n=1
while True:
        savol = f"{n}-tabingizdagi ovqatni kiriting: "
        menular = input(savol)
        menu.append(menular)
        javob = input("Yana ovqat kiritasizmi? (ha\yo'q)")
        if javob == 'ha':
            n+=1
            continue
        else:
            break
        
        print("Ovqatlar ro'yxati:")
        for menular in menu:
            print(menular.title()) 