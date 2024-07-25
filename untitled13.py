lugat = {
         'integer':'butun son',#1
         'len':'royxat uzunligini bilish ucun',#2
         'reverse':'royxatni aylantirish',#3
         '.sort':'tartibash',#4
         '.append':'royxatga yangi element qoshish',#5
         '.inert':'royxatning istalgaan joyiga element qoshish',#6
         'del':'bu indeks ochirib tashlash u-n',#7
         '.upper':'harflarni katta qilib yozadi',#8
         '.title':'sozning bosh harfini kota qilib yozadi',#9
         '.pop':'tanlangan elementni sugurib oloadi',#10
         'tuples':'dumaloq qavs yordamida ozgarmas royxat'}#11

kalit = input('Kalit soz kiriting>>>').lower()
print(lugat.get(kalit, "Bunday so'z maavjud emas"))
kalit = input("Kalit so'zni kiriting").lower()
tarjima = lugat.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} sozi {tarjima} deb tarjima qilinadi")