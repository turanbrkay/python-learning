# "\" işaretini öğreneceğiz

print("Türkiye Cumhuriyeti Devleti \
Libya'da aktif rol oynamakta ve \
oynamaya devam ediceğini bildirmektedir")

print("""Türkiye Cumhuriyeti Devleti
her geçen gün daha da ekonomik                   
sıkıntılar içerisine düşmektedir""")

#  *** ikisi arasındaki fark birisi (\) aynı satırda devam ederken, (""") diğeri her alt satıra geçtiğinde yazdırmada da alt satıra geçmekte

komut="Central İntelligence Agency"
print(komut,"\n","-"*len(komut), sep="")

# (run: Central İntelligence Agency
#       ---------------------------  )        görüldüğü gibi çizgileri tam hizaya getirdik bunu sep ve len ile yaptık

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print("c:\Windows\northvpn")      # görüldüğü gibi bir sorunla karşılaştık.    ( run:c:\Windows
                                  #                                                  orthvpn   )

# bunu aşmak için ya iki tane \\ kullanacağız ya da normal taksim / kullanacağız
print("c:\Windows\\northvpn")     # (run: c:\Windows\northvpn)
print("c:/Windows/northvpn")      # (run: c:/Windows/northvpn)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# \t işareti (sekme)
#  bu işaret araya konulduğunda tab(sekme) basılmış gibi boşluk atıyor

# vatan ifadesini sağa doğru itti.
print("mavi\tvatan")           # (run:  mavi	vatan)


print("babam", "ve", "oğlum", "filmi","müthiş", sep="\t")
# (run: babam	ve	oğlum	filmi	müthiş)
# parametreler arasında boşluk bırakmak istediğinde \t yi kullanabilirsin

print("https:\\morutan\tasdemir\norway")    #saçmalığın daniskası düzeltelim:    (run: https:\morutan	asdemir
                                            #                                          orway                   )


print("https:\\mortan\\tasdemir\\norway")   # (run: https:\mortan\tasdemir\norway )
print("https://morutan//tasdemir//norway")  # (run: https://morutan//tasdemir//norway)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# \r "Aynı Satır Başı"
# bu işaretten sonra aynı satırda başa döner ve üstüne yazar

print("seni çok seviyorum")
print("seni çok\r seviyorum")                 #(run: seviyorum)     (cmd:seviyorum)
print("seni her zaman\rseveceğim")            #(run: seveceğim)     (cmd:seveceğimzaman)
# pycharm 2021.2.1 de bir sıkıntı var \r den sonrakini başa alıyor ancak soldaki tüm stringi siliyor ve sadece sağdakini yazıyor
# ancak bunu cmd de denediğinde cmd önce sağdakini yazdırıyor sonrasında solda kalan karakterleri yazdırıyor


print("Merhaba\rDünya")
# cmd için:
# Burada, “Merhaba” karakter dizisi ekrana yazdırıldıktan sonra \r kaçış dizisinin etkisiyle satır başına dönülüyor
# ve bu kaçış dizisinden sonra gelen “Dünya” karakter dizisi “Merhaba” karakter dizisinin üzerine yazıyor.
# Tabii “Dünya” karakter dizisi içinde 5 karakter, “Merhaba” karakter dizisi içinde ise 7 karakter olduğu için,
# “Merhaba” karakter dizisinin son iki karakteri (“ba”) dışarda kalıyor. Böylece ortaya “Dünyaba” gibi bir şey çıkıyor.


print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

# \v (düşey sekme)
# çoğu yerde çalışmıyor bu çok önemli değil

print("bir\viki\vüç\vdört")
#burada çalışmıyor normalde yapması gereken
# (run: bir
#          iki
#             üç
#               dört  )

print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

# \b (İmleç Kaydırma) işareti
# imleci bir tık sola kaydırıyo ve yazdırmaya oradan devam ediyor

print("google.com\b.tr")            # (run:google.co.tr)    görüldüğü üzere m harfi boşa gitti
print("seni seviyorum\b\bdum")      # (run:seni seviyordum) böyle düzeltmeler yapabiliriz :)

print("https://","github",".com")        # ayrı yazdı (run:https:// github .com) , birleştirmek için:
print("https://","\bgithub","\b.com")    # birleştirdik (run:https://github.com) ama bu uzun yol onun yerine sep** kullan gitsin

print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

# küçük unicode (\u)
# unicode kavramı önemli ama kısaca şöyleymiş, her harf tek ve benzersiz bir kodla belirlenmiş
# unicode sisteminde "ı" harfi  u+0131 bu şekide kodlanmış
# a harfi ise u+0061 bu şekilde

# Python programlama dilinde ise, yukarıdaki kod konumu düzeni şöyle gösterilir: aradaki + kalkacak
# örneğin: ȹ bu işaret için \u0239 yazman gerekiyor
print("\u0239")       # (run: ȹ )
# örneğin: E harfi için \u0045 yazman lazım
print("\u0045")       # (run: E )

print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

# büyük unicode (\U)
# Bu kaçış dizisi biraz önce gördüğümüz \u adlı kaçış dizisiyle hemen hemen aynı anlama gelir.
# Bu kaçış dizisi de, tıpkı \u gibi, UNICODE kod konumlarını temsil etmek için kullanılır
# . Ancak U ile gösterilen kod konumları u ile gösterilenlere göre biraz daha uzundur.
# 8 haneli (U dan sonra 8 hane)
# örneğin E harfi için \u0045 yazmak lazımdı, büyük unicode da ise \U00000045 yazman lazım
print("\U00000045")     # (run: E )
print("\u0045")         # (run: E )
# küçük unicode da ise (\u) 4 hane var u dan sonra

# karakterlerin unicode kodlar için https://unicode-table.com/en/ bu sayfa iyi, internette bulabilirsin yine

print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

# uzun ad (\N)
# çok saçma geldi bana neden kısası varken uzununu kullanayım?
# bu da unicode sistemi ile ilgili
# mantığı bir harfin veya karakterin unicode daki uzun ismini kullanırken bize yardımcı oluyor.

# Bir karakterin UNICODE sistemindeki uzun adını öğrenmek için "unicodedata" adlı bir modülden yaralanacağız

# bu pycharm da denediğinde olmaz ama cmd de denediğinde oluyor yazman gereken::::
#  import unicodedata
#  unicodedata.name("a")
#  bu ikisini yazdığında cmd sana şöyle cevap verir: 'LATIN SMALL LETTER A'

#  import unicodedata
#  unicodedata.name("5")
#  bu ikisini yazdığında cmd sana şöyle cevap verir: 'DIGIT FIVE'
#   unicode sistemindeki adı buymuş

# şimdi \N kullancağız ve uzun adı kısasına çevireceğiz
print("\N{LATIN SMALL LETTER A}")             # (run: a )
print("\N{DIGIT FIVE}")                       # (run: 5 )

# print("\Nisan")    bu şekilde yazamıyorsun çünkü \N başka bir anlam taşıyor tavsiyem / yap geç. \ bu sıkıntı

# kitap yazarı tarafından uyarı!
# Bildiğiniz gibi Windows 7’de kullanıcının dosyalarını içeren dizin adı C:\Users\kullanıcı_adı şeklinde gösteriliyor.
# Dolayısıyla Windows kullananlar UNICODE kaçış dizilerinden kaynaklanan bu tuzağa her an düşebilir.
# Ya da eğer adınız ‘u’ veya ‘n’ harfi ile başlıyorsa yine bu tuzağa düşme ihtimaliniz epey yüksek olacak,
# C:\Users\umut veya C:\Users\Nihat gibi bir dizin adı belirtirken çok dikkatli olmanız gerekecektir.
# Zira özellikle dosyalar üzerinde işlem yaparken, bu tür dizin adlarını sık sık kullanmak durumunda kalacaksınız.
# Bu yüzden, alelade bir kelime yazdığınızı zannederken hiç farkında olmadan bir kaçış dizisi tanımlıyor olma ihtimalini
# her zaman göz önünde bulundurmalı ve buna uygun önlemleri almış olmalısınız.

print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

# Onaltılı Karakter (\x)
# sanırsam bu da unicode gibi bir karakter sistemi
# örneğin \x43 yazdığında C harfi elde ediyorsun
print("\x43")          # (run: C)
print("\x3F")          # (run: ?)
# bu siteden daha ayrıntılı bulabilirsin:: https://ascii.cl
# bazılarını pycharm da görüntüleyemiyorum

print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

# Etkisizleştirme (r)
# \nisan vb. yazıları \n algılamasın diye \\nisan veya /nisan yazıyorduk bunun daha kolay bir yolu var

print("c:\nisan\farklı\biliyorsun")
# bunun düzeltmek için
print("c:\\nisan\\farklı\\biliyorsun")     # (run: c:\nisan\farklı\biliyorsun)
# veya
print("c:/nisan/farklı/biliyorsun")        # (run: c:/nisan/farklı/biliyorsun)
# veya basiti
print(r"c:\nisan\farklı\biliyorsun")       # (run: c:\nisan\farklı\biliyorsun )
# Gördüğünüz gibi, karakter dizisinin baş kısmının dış tarafına bir adet r harfi yerleştirerek sorunun üstesinden geliyoruz
# r harfinin tırnağın dışında olduğuna dikkat et, ayrıca tırnağa birleşik o da önemli!

print(r" \n \b \v \a \f ")                  # (run: \n \b \v \a \f )

#  bu kaçış dizisini, daha önce öğrendiğimiz \r adlı kaçış dizisi ile karıştırmamaya dikkat ediyoruz. \r satır başı yapıyordu üstüne yazma falan


# bir ayrıntı::
# Python’da karakter dizilerinin sonunda sadece çift sayıda \ işareti bulunabilir.
# Tek sayıda \ işareti kullanıldığında karakter dizisini bitiren tırnak işareti etkisizleşeceği için çakışma sorunu ortaya çıkar.
# Bu etkisizleşmeyi, karakter dizisinin başına koyduğunuz ‘r’ kaçış dizisi de engelleyemez.
# print("Kaçış dizisi: \")
# Bu şekilde bir tanımlama yaptığımızda Python bize bir hata mesajı gösterir.
# Çünkü kapanış tırnağının hemen öncesine yerleştirdiğimiz \ kaçış dizisi,
# Python’ın karakter dizisini kapatan tırnak işaretini görmezden gelmesine yol açarak bu tırnağı etkisizleştiriyor.
# Böylece sanki karakter dizisini tanımlarken kapanış tırnağını hiç yazmamışız gibi bir sonuç ortaya çıkıyor
# Üstelik bu durumu, r adlı kaçış dizisi de engelleyemiyor
# çözüm olarak ya bir adet boşluk bırak ya da iki tane \\ kullan
print("Kaçış dizisi: \ ")
print("Kaçış dizisi: \\")
# ya da
print("Kaçış dizisi: " + "\\")
print("Kaçış dizisi:", "\\")
print("Kaçış dizisi: " "\\")
# hepsi aynı sonucu verir (run:Kaçış dizisi: \)

print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

# SON OLARAK KAÇIŞ DİZİLERİNE KİTAPTAN ALINTILADIĞIM TOPLU BAKIŞ

#     \’        Karakter dizisi içinde tek tırnak işaretini kullanabilmemizi sağlar.

#     ”         Karakter dizisi içinde çift tırnak işaretini kullanabilmemizi sağlar.

#     \\        Karakter dizisi içinde \ işaretini kullanabilmemizi sağlar.

#     \n        Yeni bir satıra geçmemizi sağlar.

#     \t        Karakterler arasında sekme boşluğu bırakmamızı sağlar.

#     \u        UNICODE kod konumlarını gösterebilmemizi sağlar.

#     \U        UNICODE kod konumlarını gösterebilmemizi sağlar.

#     \N        Karakterleri UNICODE adlarına göre kullanabilmemizi sağlar.

#     \x        Onaltılı sistemdeki bir sayının karakter karşılığını gösterebilmemizi sağlar.

#     \a        Destekleyen sistemlerde, kasa hoparlöründen bir ‘bip’ sesi verilmesini sağlar.

#     \r        Aynı satırın başına dönülmesini sağlar.

#     \v        Destekleyen sistemlerde düşey sekme oluşturulmasını sağlar.

#     \b        İmlecin sola doğru kaydırılmasını sağlar

#     \f        Yeni bir sayfaya geçilmesini sağlar.

#      r        Karakter dizisi içinde kaçış dizilerini kullanabilmemizi sağlar.