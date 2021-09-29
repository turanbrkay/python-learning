import sys

print("hello world")

print("hacettepe","üniversitesi")          # (run:hacettepe üniversitesi)

print("hacettepe"+"üniversitesi")          # (run:hacettepeüniversitesi)
print("hacettepe"+" "+"üniversitesi")      # (run:hacettepe üniversitesi)

print("istanbul"+"1453")                   #(run:istanbul1453)
#print("istanbul"+1453)      bu şekilde yazdıramazsın çünkü biri string biri int, ikisinide aynı değişken yapmalısın.
print("istanbul"+str(1453))                #(run:istanbul1453)
print("istanbul",1453)                     #(run:istanbul 1453)

#print("8"+5)                   bu şekilde de toplamaz çünkü aynı değerde olmalı
print(int("8")+5)               #(run:13)
print("8"+str(5))               #(run:85) burada 8 ve 5 i yazı olarak görüp birleştiriyor string olduğu için toplama yapmıyor yan yana getiriyor.

#print("8.5"+3)                 yazdıramazsın
print(float("8.5")+3)                      #(run:11.5)   burada floatla int neden toplandı dersen ikiside sayı olduğu için. yazı ile sayı toplanmaz ama sayı ile sayı toplanabilir ondalık olması farketmez.
# print(int("8.5")+3)           #  8.5 i floatla yazdırabilirken int olarak alamıyorum. Yapmak istediğim string değeri olan"8.5" i int fonksiyonu kullanarak 8 olarak almak ve 3 ile toplamaktı ancak stringi int e dönüştüremiyorum bunun nedeni string deki değerin ondalık sayı olmasından kaynaklanıyor muhtemelen.

print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

print("""                        
tcganadolu                
""")

#aynı şeyi tek tırnakla yapamayız,çift tırnağın üç kere tekrarlanması zorunlu.

print(""""
***************************************
**                CİA                **  
** Department:                       **  
** ID Number:                        **          
** Status:                           **       
** Password:                         **
***************************************
""")

print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

#sep parametresi

print("https", "://", "twitter", ".com")                    #(run:https :// twitter .com)
#Burada herhangi bir sep parametresi görmüyoruz. Ancak Python yukarıdaki kodu aslında şöyle algılar:
print("http://", "www.", "google.", "com", sep=" ")         #(run:https :// twitter .com)  üstteki gibi algılıyor

#  Bu parametrenin öntanımlı değeri bir adet boşluk karakteridir (” “).
#  Yani siz bu özel parametrenin değerini başka bir şeyle değiştirmezseniz,
#  Python bu parametrenin değerini bir adet boşluk karakteri olarak alacak ve ekrana basılacak öğeleri birbirinden birer boşlukla ayıracaktır.
#  Ancak eğer biz istersek bu sep parametresinin değerini değiştirebiliriz.
#  Böylece Python, karakter dizilerini birleştirirken araya boşluk değil, bizim istediğimiz başka bir karakteri yerleştirebilir.

print("https", "://", "twitter", ".com",sep="")  #sep parametresi ile aradaki boşluğu kaldırdık (run:https://twitter.com)

print("" , "berber", "berbere","kere", "vermiş",sep="bir")   #  (run:birberberbirberberebirkerebirvermiş)
print("" , "berber", "berbere","kere", "vermiş",sep=" bir ") #  (run: bir berber bir berbere bir kere bir vermiş)

print(1,2,3,4,5, sep="*")      #(run:1*2*3*4*5)

# sep parametresine değer olarak yalnızca karakter dizilerini ve None adlı özel bir sözcüğü verebiliyormuşuz.
# yani parantez açman gerekiyor direkt 0 yazmazsın

print(1,2,3,4,sep="0")        #(run:1020304)
#print(1,2,3,4,sep=0)         olmuyor

# bir parametreye None değeri verilirse orada bir adet boşluk(öntanımlı değeri) oluşuyor
print("harvey","specter","suits",sep=None)            #(run:harvey specter suits)
# gidipte sep="None" yazma bu şekilde karakter dizisi oluyor araya None yazdırıyorsun.

print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

# end parametresi
#print() fonksiyonunun end adlı özel bir parametresi daha bulunur.
# Tıpkı sep parametresi gibi, end parametresi de print() fonksiyonunda görünmese bile her zaman oradadır.
#Bildiğiniz gibi, sep parametresi print() fonksiyonuna verilen parametreler birleştirilirken araya hangi karakterin gireceğini belirliyordu.
# end parametresi ise bu parametrelerin sonuna neyin geleceğini belirler.
# varsayılan değeri \n dir

print("messigoat")

print("messithebest",end="///")
print("always")
# burada görüldüğü üzere ilk yazdırdığımız komuttan sonra end değeri \n olduğu için bir alt satıra geçti ancak sonrasında
# end değerini /// yaptığım için araya bu işareti koyup bir sonraki komutu yazdırmaya devam etti,
# yani end den varsayılan değerini alıp yerine /// koydum
# (run:messigoat           )
# (    messithebest///always)

#kısaca
print("Bugün günlerden Salı")
#aslında python bu ifadeyi şu şekilde algılar
print("Bugün günlerden Salı", end="\n")
#ikisi de aynı şey.

print("","berber","berbere","kere","lira",
      sep=" bir ",end=" vermiş.\n")                  # virgül koyup bir alt satıra inebiliriz (run:bir berber bir berbere bir kere bir lira vermiş.)

# Yine tıpkı sep parametresi gibi, end parametresinin değeri de sadece bir karakter dizisi veya None olabilir
# yani None verdiğimide end ifadesi bunu \n olarak aldılayacak (varsayılan değeri)


print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

# file
# Görevi , print() fonksiyonuna verilen karakter dizisi ve/veya sayıların, yani parametrelerin nereye yazılacağını belirtmektir.
# örneğin biz print() e bir yazı yazdığımızda komut satırında bize gösteriyor ancak bunun nerede gösterileceğini belirleyen file,
# sep ve end gibi bu da gizli
# bu parametrenin varsayılan değeri (sys.stdout) dur. ‘standart çıktı konumu’ anlamına gelir.
# standart çıktı konumu = çıktıların standart olarak verildiği konum
# Eğer o anda etkileşimli kabukta çalışıyorsanız, Python ürettiği çıktıları etkileşimli kabuk üzerinde gösterir.
# Eğer yazdığınız bir programı komut satırında çalıştırıyorsanız, üretilen çıktılar komut satırında görünür

print("hello world")     # bu ifadeyi komut satırında görürüz

# Ama eğer istersek print() fonksiyonunun, çıktılarını ekrana değil, bir dosyaya yazdırmasını da sağlayabiliriz.
# Mesela biz şimdi print() fonksiyonunun deneme.txt adlı bir dosyaya çıktı vermesini sağlayalım.

yenidosya= open("deneme.txt","w")
print("hello world", file=yenidosya)
yenidosya.close()
# gördüğün üzere herhangi bir çıktı almadık, yeni bir txt dosyası oluşturuldu ve yazdığımız komut orada oluştu
# burada sonda dosyayı kapatmayı unutma
# ileride zaten öğreneceksin "w" de önemli

# peki normalde python bunu varsayılan olarak nasıl algılıyor


print("greencard","canada")
print("greencard","canada",file=sys.stdout)              # ikisi de aynı şey.

print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")



import keyword
keyword.kwlist           # bu iki satırı yazdığınızda pythondaki özel kelimeleri göreceksin (etkileşimli kabuğa yazman gerekli) (bu keliemlere değer veremezsin)
print(keyword.kwlist)    # print ile run yaptığında da bunların listesini göreceksin

print(len(keyword.kwlist))   # bu liste 36 karakterden oluşuyormuş


# pow fonsiyonu
# üslü ifadeyi bununla da alabilirsin

print(pow(12, 2))   # (run:144)
print(pow(15, 2))   # (run:225)
print(12**2)        # (run:144) pow la aynı şey

print(pow(12,2,2))             # bunun anlamı 12 nin 2 ile üssünü al çıksan sonucu 2 ye böl ve kalanını söyle
print(int(pow(144, 0.5)))      # bir sayının 0.5 katı onun karekökü biliyorsun

print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
# nisan ayı ortalama elektrik faturası tutarı hesaplama
nisan=30
mart=31
aylıktüketim=420
martücret=280

günlüktüketim=aylıktüketim/mart
nisantüketim=günlüktüketim*nisan
print(nisantüketim)    # faturamız 406.4516129032258tl gelecek

print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

firmino= "ilk 11"
salah= "yedek"
print(firmino,salah)

firmino,salah=salah,firmino   # yerlerini kolay bir şekilde değiştirdik
print(firmino,salah)


print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

# yıldız parametresi

print(*"ATATURK")           #(run:A T A T U R K)
# başa yıldız getirdiğinde tüm karakterleri ayırıyor

print(*"ATATURK", sep=".")  #(run:A.T.A.T.U.R.K)
# bu işlem aralara koyulan işareleri kolaylaştırıyor

print(*"TBMM", sep=".")    #(run:T.B.M.M)

#yıldızlı parametreleri sayılarda kullanamazsın.
#print(*121154) olmaz

print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")









