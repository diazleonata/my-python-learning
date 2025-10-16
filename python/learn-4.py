# loop
# x = 1
# while x < 100:
#     print(x)
#     x += 1

# loop with ganjil genap
# x = 1

# while x < 100:
#     if x % 2 == 0:

#         print(f"{x} adalah bilangan genap")
#     else:
#         print(f"{x} adalah bilangan ganjil")
#     x += 1 

# loop with function
def ganjilGenap(x):
    if x % 2 == 0:
        ket = "Bilangan Genap"
    else:
        ket = "Bilangan Ganjil"
    return ket

x = 1

while x < 101:
    ket = ganjilGenap(x)
    print(f"{x} adalah {ket}")
    x += 1
    
kata = "Algoritma"
for huruf in kata:
    if huruf == 'x':
        continue
    print(huruf)
    
print ("tebak huruf")
while True:
    inputhuruf = input("masukkan huruf : ")
    if inputhuruf.lower() == 'f':
        print("tebakan anda benar")
        break
    else:
        print("tebakan anda salah, silahkan coba lagi")