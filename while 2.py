#e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
#Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

# mevani nomi keyn mevani narhini yozish kere 
mahsulotlar = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting: ")
    narh = input("Mahsulot narhini kiriting")  
    mahsulotlar[mahsulot] = narh
    javob = input("Yana mahsulot qo'shamzmi ha\yo'q")
    if javob != "ha":
        break 