print("5*2 işleminin sonucu nedir?",5*2)
print("5+4 işleminin sonucu nedir?",5+4)
print("4-5 işleminin sonucu nedir?",4-5)

print("-------------------------------------------------------------------")

print("4/4 işleminin sonucu nedir?",4/4)   # Ondalık sayı çıkıyor (1.0)
# Bölmeler de yazdırdığımızda tam sayı çıkmasını istiyorsak iki yöntem kullanabiliriz
# İlki // kullanmak
# İkinicisi int fonksiyonunu kullanmak (int = tam sayı , float= ondalık )
print("4/4 işleminin sonucu nedir? (//)",4//4)         # Tam sayı çıkıyor (1)
print("4/4 işleminin sonucu nedir? (int)",int(4/4))    # Tam sayı çıkıyor (1)

# 5/4 işlemini float ve int fonksiyonlarını kullanarak yapalım.
print("5/4 işlemini float ile yapınız.",float(5/4))
print("5/4 işlemini int ile yapınız.",int(5/4))
# int tam sayı çıkardı, float ondalık çıkardı
# int, integerın kısaltmasıdır integer tamsayı demektir.


print("4**3 işleminin sonucu nedir?",4**3)
# burada ** işlemi üslü ifade anlamına gelmektedir


print("15/2 işleminde kalan nedir?",15 % 2)
# kalanı bulmak için python da % işareti kullanılır.

print("------------------------------------------------------------------------------")

# şimdi bazı örnekler yapalım
x=8
y=4
print("x+y ifadesinin sonucu nedir?",x+y)
print("x*15 ifadesinin sonucu nedir?",x*15)

print("-------------------------------------------------------------------------------------")

a=10
b=4
c=a+b
print("c nedir?", c)

print("-------------------------------------------------------------------------------------")



# daire alanı hesaplayacağız
# takıldığın nokta pi sayisi yazman. Araya boşluk bırakmayacaksın pisayisi veya pi_sayisi olmalı.
# alanı tanımlarken yaricapi parantez icine alman önemli
pi_sayisi= 3.14
yaricap= 4

alan= pi_sayisi*(yaricap**2)
print("dairenin alanı nedir?", alan)













