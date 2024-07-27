#Python izohli lug'atini yaratish va lug'atga kamida 10 ta so'z qo'shish. 
#Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, 
#alifbo ketma-ketligida chiroyli qilib konsolga chiqarish

izohli_lugat = {
                'Boolean':'Mantiqiy qiymat',#1
                'Float':'o\'nlik son',
                'Integer':'Butun son',
                'for':'biror amalni qayta bajarish tsikli',
                'if':'shartlarni tekshiruvchi',
                'else':'if ga qo\'shimcha',
                'elif':'if va else yig\'gindisi'
                }
for kalit, qiymat in sorted(izohli_lugat.items()):
    print(f"{kalit.title()} - {qiymat}\n")