
hitabe = open("gencligehitabe.txt", encoding="utf-8")   # dosyamızı açtık ve utf-8 ile türkçe karakterleri pythona tanıttık

harf=input("Sorgulamak istediğiniz harfi girin...")
sayi = 0

for karakter_satır in hitabe:              # hitabenin içindeki karakterleri karakter_Satır adlı yere alıyoruz ancak bir sorun var.
                                           # Bu alım ile sadece metni satırlara ayırabiliyoruz. Eğer harflere ayırmak istiyorsan iç içe iki tane for döngüsü kullanman gerekiyor.
    for karakter in karakter_satır:
        if karakter == harf:
            sayi += 1

print(sayi)

hitabe.close()