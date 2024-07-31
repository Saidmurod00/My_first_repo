taomlar = {
            'osh':41000,
            "lag'mon":30000,
            "kuksi":31000,
            "sho'rva":39000,
            'limonad':15000,
            "Coca-cola": 8000,
            'fanta': 8000,
            'sprite': 8000,
            'salat':20000,
            'salat baxoriy':21000,
            }
print("3 ta taom buyurtma bering:>>>")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())
    
for buyurtma in buyurtmalar:
    if buyurtma in taomlar:
        print(f"{buyurtma.title()} {taomlar[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")