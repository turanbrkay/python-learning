# burada yaptığımız şey öncelikle bir döngü oluşturuyoruz. firminoyu bir bir artırıyoruz, 10 olduğunda while döngüsü duruyor ve if bloğu çalışıyor.


firmino=1

print("Firmino'nun şuanki seviyesi:", firmino)


while firmino < 10:
    print("Firmino, yeterli seviyeye ulaşamadın!")
    firmino += 1
    print("Firmino'nun şuanki seviyesi:",firmino)
    if firmino == 10:
        print("Şimdi seni ilk 11'e alabilirim.")

