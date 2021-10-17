# burada kullanıcıdan cümleler alıyoruz ve cümleleri karşılaştırıyoruz farklı karakterler varsa bunu ekrana yazdırıyoruz.


karakter1=input("Karşılaştırma yapmak istediğiniz ilk karakterleri giriniz...")
karakter2=input("Karşılaştırma yapmak istediğiniz ikinci karakterleri giriniz...")



for karsılastırma in karakter1:
    if not karsılastırma in karakter2:
        print(karsılastırma)



for karsılastırma2 in karakter2:
    if not karsılastırma2 in karakter1:
        print(karsılastırma2)