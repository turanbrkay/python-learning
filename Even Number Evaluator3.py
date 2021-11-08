print("""
//////////////////////////////////////////////////    
//    Çift Sayı Değerlendiriciye Hoşgeldiniz!   //
//////////////////////////////////////////////////     

Sizden 5 tane farklı TAM SAYI girmenizi istiyoruz:

""")
import time

while True:

    while True:
        try:
            first = int(input("İlk sayıyı giriniz:"))
            if first < 0:
                print("0'dan büyük bir sayı girmelisiniz!!\nTekrar deneyin..")
            else:
                break
        except ValueError:
            print("TAM SAYI girmelisiniz!!\nLütfen tekrar deneyin..")
            continue

    while True:
        try:
            second = int(input("İkinci sayıyı giriniz:"))
            if second < 0:
                print("0'dan büyük bir sayı girmelisiniz!!\nTekrar deneyin..")
            elif first == second:
                print("Lütfen farklı bir sayı giriniz!!")
            else:
                break
        except ValueError:
            print("TAM SAYI girmelisiniz!!\nLütfen tekrar deneyin..")
            continue

    while True:
        try:
            third = int(input("Üçüncü sayıyı giriniz:"))
            if third < 0:
                print("0'dan büyük bir sayı girmelisiniz!!\nTekrar deneyin..")
            elif first == third or second == third:
                print("Lütfen farklı bir sayı giriniz!!")
            else:
                break
        except ValueError:
            print("TAM SAYI girmelisiniz!!\nLütfen tekrar deneyin..")
            continue

    while True:
        try:
            fourth = int(input("Dördüncü sayıyı giriniz:"))
            if fourth < 0:
                print("0'dan büyük bir sayı girmelisiniz!!\nTekrar deneyin..")
            elif first == fourth or second == fourth or third == fourth:
                print("Lütfen farklı bir sayı giriniz!!")
            else:
                break
        except ValueError:
            print("TAM SAYI girmelisiniz!!\nLütfen tekrar deneyin..")
            continue

    while True:
        try:
            fifth = int(input("Beşinci sayıyı giriniz:"))
            if fifth < 0:
                print("0'dan büyük bir sayı girmelisiniz!!\nTekrar deneyin..")
            elif first == fifth or second == fifth or third == fifth or fourth == fifth:
                print("Lütfen farklı bir sayı giriniz!!")
            else:
                break
        except ValueError:
            print("TAM SAYI girmelisiniz!!\nLütfen tekrar deneyin..")
            continue



    kullaniciverileri = [first, second, third, fourth, fifth]
    kumekullaniciverileri = set([first,second,third,fourth,fifth])

    print("Giriş başarılı.\nHesaplamalar yapılıyor...")


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




