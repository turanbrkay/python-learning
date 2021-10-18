# bu iki değeri kullanarak kullanıcıya verilecek hata mesajını kontrol edebiliyoruz
# örneğin aşağıda yazacağımız bölme işleminde kullanıcıdan biz sayı değeri girmesini bekliyoruz
# eğer kullanıcı sayı yerine harf girerse ValueError hatası verir python
# eğer kullanıcı bir sayıyı sıfıra bölmeye çalışırsa ZeroDivisionError hatası verir python
# işte böyle hatalarla karşılaştığımızda ValueError veya ZeroDivisionError yerine daha açıklayıcı şeyler yazmak için try ve except i kullanacağız




ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ValueError:
    print("Sadece sayı girmelisiniz..")
except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsiniz..")

# python a dedik ki eğer try bloğu içerisinde valueerror hatası alırsan print çıktısını ver. hatalar için aynı çıktıyıda verdirebilirdik
# örneğin:

# except (ValueError,ZeroDivisionError):
#   print("Bir hata bulundu.")


