kitoblar = "Sevimli kitoblaringiz ro'yxatini kiriting: "
kitoblar += "Sevimli kitoblaringizni kiritib bo'lgach exit deb yozing "
kitoblar()
while True:
    kitob = input(kitoblar)
    if kitob == "exit":
        break
print("Raxmat")

print(kitoblar)