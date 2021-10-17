# range fonksiyonu ile parolanın karakter limitini belirleyebiliriz.

while True:
    parola=input("Parolanızı girin..:")

    if not parola:
        print("Parola bölümü boş geçilemez..")

    elif len(parola) in range(4,8):
        print("Parolanız oluşturulmuştur.\nParolanız: {}".format(parola))
        break

    else:
        print("Parolanız 3 karakterden uzun 8 karakterden kısa olmalıdırr..")

# istesek burada for ile izinli karakterler yapıp kullanıcıdan sadece belirli karakterleri alabilirdik.