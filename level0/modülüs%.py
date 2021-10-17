# yüzde işareti bölme işleminden kalanı bulur

bölünen=int(input("Bölmek istediğiniz sayıyı girin."))
bölen=int(input("Sayıyı bölmek istediğiniz böleni girin."))

islem="{} sayisi {} sayisina tam".format(bölünen,bölen)

if bölünen % bölen == 0:
    print(islem,"bölünüyor.")
else:
    print(islem,"bölünmüyor.")

# Kullanıcıdan bölünen ve böleni alıp birbirine tam bölünüp bölünmediğini çıkartırıyoruz.