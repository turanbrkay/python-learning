# kullanıcıdan aldığı aralıkta tek sayıları bulan program

print("""
          Sizden iki tane sayı isteyeceğiz 
    Bu sayılar 0 dan büyük 500'den küçük olmalıdır.
    İlk girdiğiniz sayı ikinciden küçük olmalıdır..
Yazdığınız aralıktaki tek sayıları programımız yazdıracaktır

""")

sayi1=int(input("İlk sayıyı girin.."))
sayi2=int(input("İkinci sayıyı girin.."))


#sayıları 0 ve 500 arasında seçtiriyoruz.
if 0<sayi1<500 and 0<sayi2<500 and sayi1<sayi2:
    while True:                                                     # döngüyü açtım break ile de kapattım
        sayi1+=1
        if sayi1%2==1:
            print(sayi1)
        elif sayi1==sayi2:                                          # sayi1 ile sayi2 eşitlenince döngüyü kapattım.
            print("Program aralıktaki tüm tek sayıları yazdırdı...")
            break
else:
    print("Hatalı giriş yaptınız! Belirtilen şekilde giriş yapın..")


input()