# burada yaptığımız şey oluşturduğumuz parolada türkçe karakterler kullanmamak üzerine

tr_harf="şçöğüİı"

parola=input("Enter the password you want to create..")

for notrkarakter in parola:
    if notrkarakter in tr_harf:
        print("Parolanızda Türkçe karakter kullanmayınız...")

        # burada yaşadığım sıkıntı parolayı yazdığımda kaç tane türkçe karakter varsa o kadar yazı alt alta çıkıyordu

        # örneğin "ğğğğ" yazdıysam:
        # Parolanızda Türkçe karakter kullanmayınız.
        # Parolanızda Türkçe karakter kullanmayınız.
        # Parolanızda Türkçe karakter kullanmayınız.
        # Parolanızda Türkçe karakter kullanmayınız.   diye çıktı alıyordum bunu aşmak için break kullanmalısın. (for5'de yaptım)
