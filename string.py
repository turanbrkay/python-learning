a = "software science"
print(type(a))       # çıktıda a değişkeninin string olduğunu öğreniyoruz            (run:str)

print(a[0])          # a değişkeninin baştan 1. harfi için 0 ı kullanıyoruz          (run:s)
print(a[-2])         # a değişkeninin sondan 2. harfi için -2 yi kulanıyoruz         (run:c)
                     # sıralama baştan 0 ile sondan -1 ile başlıyor burası önemli

print(a[2:5])        # başlangıç ve bitiş indeksi değerlerini giriyoruz ve bize dilimleyip veriyor
                     # başlangıç indeksinin dahil olarak sayılır, bitiş indeksinin dahil olarak sayılmaz.   (run:ftw)

print(a[:8])         # boşluk bıraktığımız tarafın tüm yazılarını alır              (run:software)
print(a[4:])         #                                                              (run:ware science)
print(a[:])          #                                                              (run:software science)


print(a[1:12:2])     #belirlediğiniz aralıktaki tüm karakterleri değil, başlangıç karakterinden 2 karakter arayla aldık.
                     # 1. karakterden 12. karaktere kadar 2 karakter arayla aldık   (run:otaesi)



# b= "market"        (run : TypeError: 'str' object does not support item assignment)
# b[0]= "p"          string veri tipine sahip değişkenlerin karakterleri değiştirilemez/güncellenemez. Yenisi atanabilir.
# print(b)


c="kamikaze"
print(c)             # (run: kamikaze)

c="donerkanat"
print(c)             # (run: donerkanat)  aynı değişkene farklı bir yeni değer atadık.

print("***********************************************************************************************************")

print(a)
del a                 # String veri tipine sahip değişkenleri “del” fonksiyonu ile tamamen kaldırabilirsiniz. Kaldırılan değişken, tekrar çağrıldığında “NameError” hatası alınır.
#print(a)             (run: NameError: name 'a' is not defined)     a değişkeni silindi.

print("***********************************************************************************************************")

ornek_1= "f16fightingfalcon"
print(len(ornek_1))                    # Bir dizenin kaç karakterden oluştuğunu bulmak için len() fonksiyonu kullanılır.

print("***********************************************************************************************************")

first_str= "mustafa"
second_str= "kemal"
third_str= "atatürk"

print(first_str + second_str)               # (run:mustafakemal) araya boşluk atmak için " " kullan (ayrı olacak " " )
print(first_str+" "+second_str)             # (run:mustafa kemal)

print(first_str+"  "+second_str+"  "+third_str)   #(run:mustafa  kemal  atatürk)

print(third_str * 3)                       # (run:atatürkatatürkatatürk) araya boşluk gelmesi lazım bunun için:
print((third_str+ " " )* 3)                # parantez içine alıp atatürk ifadesine boşluk ekledim ve öyle çarptım  (run : atatürk atatürk atatürk )


print("***********************************************************************************************************")

# print('Ali'nin evi güzel')                buradaki sorunu çözmek için ali'nin derken ki karakteri etkisizleştirmeliyiz

print('Ali\'nin evi çok güzel')             # bu işlemi \ ifadesiyle yapıyoruz buna kaçış karakteri diyoruz
print('Ali\'nin, Ayşe\'nin ve Arda\'nın evleri güzel')

#   Kaçış karakterleri
#   \’	Tek tırnak
#   \”	Çift tırnak
#   \\	Ters eğik çizgi (backslash)
#   \	Çok satırlı stringlerde yeni satır
#   \t	tab (yatay boşluk)
#   \n	Satır başı

print("ad:james\nsoyad:rodriges\ntakım:FC bayern")   # \n kullanışlı :)

print("*************************************************************************************************")

print("Bu yazıda {} konusu işlendi." .format("string"))
print("en sevdigim futbolcular {} ve {} dir" .format("robertofirmino", "jamesrodriges")) #formatta ikisinide ayrı ayrı paranteze almayı unutma

oyun1="csgo"
oyun2="valorant"
print("{en_sevilen} oyununu {az_sevilen} oyunundan daha çok severim".format(en_sevilen = oyun1, az_sevilen = oyun2))  #nedense - işareti kullandığım için uzun süre uğraştım - kullanılmıyor _ kullan.

#format için {} işareti önemli.
