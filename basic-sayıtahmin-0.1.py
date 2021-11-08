import random
sayimiz = random.randint(1,100)

for i in range(9):
    kullanicisayisi=int(input("Aklından Geçen sayıyı gir.."))
    if sayimiz<kullanicisayisi:
        print("*"*32,"\nDaha küçük bir sayı girmelisin!!",sep="")
    elif sayimiz>kullanicisayisi:
        print("*"*32,"\nDaha büyük bir sayı girmelisin!!",sep="")
    elif sayimiz==kullanicisayisi:
        print("TEBRİKLERR!! Aklımdaki Sayıyı Buldun.")
    else:
        print("Deneme Hakkın Bitti. Şansız Günündesin :(")


