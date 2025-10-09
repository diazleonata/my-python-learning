bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))
bil3 = int(input("Masukkan bilangan ketiga: "))

if bil1 > bil2 and bil1 > bil3:
    print(f"Bilangan terbesar adalah Bilangan Pertama --> {bil1}")
elif bil2 > bil1 and bil2 > bil3:
    print(f"Bilangan terbesar adalah Bilangan Kedua --> {bil2}")
else:
    print(f"Bilangan terbesar adalah Bilangan Ketiga --> {bil3}")