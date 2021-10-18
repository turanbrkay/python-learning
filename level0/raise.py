# raise deyimiyle kullanıcıya programda hata olmasa da istediğimiz hata mesajını gösterebiliyoruz. örneğin:

bölünen = int(input("bölünecek sayı: "))

if bölünen == 55:
    raise Exception("55 sayısı uğursuz, bu sayıyı kullanma.")   # araya hata mesajımızı ekledik raise ile birlikte exception da kullandık
                                                                # exception yerine her şey gelemez. NameError, TypeError, ZeroDivisionError, IOError, vb gibi şeyler gelebilir.
bölen= int(input("bölen sayı: "))


print(bölünen/bölen)