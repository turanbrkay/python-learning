# verilen sayılar ile daire alanı hesaplayalım

daireyaricap=int(input("Dairenin yarıçapını cm türünden giriniz.."))
pi=3.14
alan=(daireyaricap * daireyaricap) * pi
print(alan)

# kullanıcıdan aldığımız veri normalde str ama biz onu int yaptık böylece çarpabildik




yaricap=input("Dairenin yarıçapını cm türünden giriniz..")
sonyariçap=int(yaricap)
pi=3.14
alan= (sonyariçap * sonyariçap) * pi
print(alan)
# bu şekilde de yapabiliriz ama yariçapı aldıktan sonra int e dönüştürmeyi unutma
# bunu sonyariçap diye bir başlığın altında yaptık sadece int(yaricap) yaparsak olmuyor

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////

çap = input("Dairenin çapı: ")
yarıçap = int(çap) / 2
pi = 3.14
alan = pi * (yarıçap * yarıçap)
print("Çapı", çap, "cm olan dairenin alanı: ", alan, "cm2'dir")