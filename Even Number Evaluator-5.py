import time

print("""
//////////////////////////////////////////////////    
//    ÇİFT SAYI DEĞERLENDİRİCİYE HOŞGELDİNİZ!   //
//////////////////////////////////////////////////     
    Sizden 5 tane 0 veya 0'dan büyük farklı
        TAM SAYI girmenizi istiyoruz:
//////////////////////////////////////////////////
""")

def cift_Sayı_bulucu():

    kullaniciverileri = []
    for i in range(5):

        while True:

            try:
                sira = input("{}. sayıyı giriniz: ".format(i + 1))
                sira = int(sira)

                if sira < 0:
                    print("\n0'dan büyük bir tam sayı girmelisiniz.")
                elif sira in kullaniciverileri:
                    print("\nFarklı bir tam sayı giriniz.")
                else:
                    break


            except ValueError:
                print("\nTAM SAYI girmelisiniz.")
            except:
                print("Bir hata meydana geldi. Tekrar Deneyin.")
        kullaniciverileri.append(sira)


    print("\nGiriş Başarılı\nHesaplamalar yapılıyor...")

    time.sleep(2)

    ciftsayilar = []
    for i in kullaniciverileri:
        if i % 2 == 0:
            ciftsayilar.append(i)

    print("\n")
    print("-"*50)
    print("Girmiş olduğunuz çift sayılar: ", ciftsayilar)
    print("Girdiğiniz çift sayıların toplamı: ", sum(ciftsayilar))

    cifttoplam = sum(ciftsayilar)
    tümtoplam = sum(kullaniciverileri)
    print("Çift sayı oranı: ", cifttoplam / tümtoplam)
    print("-" * 50)
    time.sleep(1)

    tekrar = input("Tekrardan hesap yapmak için 'T', uygulamadan çıkış yapmak için 'Q' tuşuna basınız\n")
    if tekrar == "T" or tekrar == "t":
        cift_Sayı_bulucu()
    else:
        print("Çıkış Yapılıyor..")
        time.sleep(2)

cift_Sayı_bulucu()




