# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 08:46:57 2024

@author: Saidmurod00 
"""
#funksiya va royxatlar

def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'karobka':karobka,
            'yil':yili,
            'narh':narhi,}
    return avto
avto1 =avto_info("GM", "Malibu", "Qora", "Avtomat", 2017)
avto2 =avto_info("Gm", "Gentra", "Oq", "Mexanika", 2016,15000)
avtolar = [avto1,avto2]
print("Onlayn bozorda mavjud bo'lgan avto mashinallar:")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narh: {narh}")
    