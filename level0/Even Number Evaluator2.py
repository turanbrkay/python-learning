print("""
//////////////////////////////////////////////////    
//    Çift Sayı Değerlendiriciye Hoşgeldiniz!   //
//////////////////////////////////////////////////     

Sizden 5 tane farklı TAM SAYI girmenizi istiyoruz:

""")
import time

while True:
    first = int(input("İlk sayıyı giriniz:"))
    second = int(input("İkinci sayıyı giriniz:"))
    third = int(input("Üçüncü sayıyı giriniz:"))
    fourth = int(input("Dördüncü sayıyı giriniz:"))
    fifth = int(input("Beşinci sayıyı giriniz:"))

    kullaniciverileri = [first, second, third, fourth, fifth]
    kumekullaniciverileri = set([first,second,third,fourth,fifth])

    print("Sayılar Kontrol Ediliyor...")


    if len(kumekullaniciverileri) != 5:
        print("Lütfen FARKLI tam sayılar giriniz..")
        continue

    for i in kullaniciverileri:
        if i < 0:
            print("Hatalı giriş yaptınız! Lütfen 0'dan büyük bir tam sayı sayı giriniz!!")
            continue

        else:
            print("Giriş başarılı.. Hesaplamalar yapılıyor..")
            break

    time.sleep(3)

    ciftsayilar = []
    for i in kullaniciverileri:
        if i%2 == 0:
            ciftsayilar.append(i)
    print("Girmiş olduğunuz çift sayılar: ",ciftsayilar)
    print("Girdiğiniz çift sayıların toplamı: ",sum(ciftsayilar))

    cifttoplam= sum(ciftsayilar)
    tümtoplam = sum(kullaniciverileri)
    print("Çift sayı oranı: ", cifttoplam/tümtoplam)
    break
time.sleep(100)




