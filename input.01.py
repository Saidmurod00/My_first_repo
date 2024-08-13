#inputni yaxshiroq tushunish uchun qo'shimcha code'lar

#<1>
ism = input("Ismingizni kiriting ")
print(f"Salom {ism.title()}")         bu cod soda shunchaki input ishlatillgan 


#<2>
ism = input("Ismingiz nma? ")
savol = f"salom {ism.title()} yoshingiz nechida?"
yosh = int(input(savol))
if yosh >=18: 
    print('sizga kirish mumkun')
else:
   print(f'sizning yoshingiz {yosh} afsuski hali yoshsiz ') 
    
#<3>

ism = input("Ismingizni kiriting ")
savol = f"Salom, {ism.title()}. yoshingiz nechida "
yosh = input(savol) 
yosh = int(yosh)
vazn = input("vazningiz necha kg ")
vazn = float(vazn)

print(f"Ismingiz {ism.title() },\n\
Sizning yoshingiz {yosh},\n\
Vazningiz esa {vazn},")