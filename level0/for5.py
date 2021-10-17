# for3 de yaşadığım sorunu düzelttim parolayı yazdığımda kaç tane türkçe karakter varsa o kadar yazı alt alta çıkıyordu
# artık sadece bir satır şeklinde uyarı gelecek aynı cümleden 10 kere çıkmıcak karşımıza

tr_harf="şçöğüİı"

parola=input("Enter the password you want to create..")

for notrkarakter in parola:
    if notrkarakter in tr_harf:
        print("Parolanızda Türkçe karakter kullanmayınız...")
        break