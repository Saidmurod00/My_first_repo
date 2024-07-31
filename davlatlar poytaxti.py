davlatlar = {
           'aqsh':"washington",
           "o'zbekiston":'toshkent',
           'rassiya':'maskva',
           'baa':'dubay',
           "qirg'iziston":'bishkek',
           }
print('Dunyo davlatlari alifbo ketma-ketligida:')
for davlat in sorted(davlatlar):
    print(davlat.upper())   
    
print("\nDavlatlar ro'yxati:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())
    
country = input("Qaysi davlat poytaxtini bilishni istaysiz:").lower()
capital = davlatlar.get(country)
if capital==None:
    print("kechirasiz bizda bunday davlat yo'q")
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} sharhi")