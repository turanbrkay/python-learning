# aylık fatura hesaplama

ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31
nisan = haziran = eylül = kasım = 30
şubat = 28

birimfiyat=1.14

print("""
/////////////////////////////////////////////////////////////////
///   Aylık Doğalgaz Borcunuzu Öğrenme Sistemine Hoşgeldiniz  ///
/////////////////////////////////////////////////////////////////
""")


hangiay=input("Lütfen hangi aya ait borcunuzu öğrenmek istediğinizi giriniz\nGireceğiniz ayı küçük harflerle yazınız...  ")
print("*"*100)
aylıktüketim=input("Lütfen ay içerisinde tükettiğiniz doğalgaz miktarını metreküp cinsinden giriniz...")

ay=eval(hangiay)

birimtüketim= int(aylıktüketim) / ay
tüketimiktar= birimtüketim * ay * birimfiyat

print("*"*100)
print("Günlük ortalama tüketiminiz: \t", birimtüketim,"\n","Fatura tutarınız:\t",tüketimiktar, "TL", sep="")

# burada patladığım nokta eval fonksiyonu.