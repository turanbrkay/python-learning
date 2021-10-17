# range fonksiyonu kullanarak bir döngünün kaç kere çalışacağını belirleyebiliriz.

for repeat in range(3):                      # Burada repeati tanımladık sayısı 0,1,2 diye artacak
    parola=input("Parolanızı girin..:")

    if not parola:
        print("Parola bölümü boş geçilemez..")

    elif len(parola) in range(4,8):
        print("Parolanız oluşturulmuştur.\nParolanız: {}".format(parola))
        break

    elif repeat==2:                          # repeat yani denememiz (0,1,2) 2 olduğunda 3 kere yanlış denemiş oluyor ve sunucudan atıyoruz.
        print("Üç kere yanlış deneme yaptınız..\n30 dakika sonra tekrar deneyiniz!!")

    else:
        print("Parolanız 3 karakterden uzun 8 karakterden kısa olmalıdırr..")