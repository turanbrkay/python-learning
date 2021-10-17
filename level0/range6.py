# etkileşimli kabukta range(10) gibi bir komut verdiğinizde range(0, 10) çıktısı aldığınızı görüyorsunuz.
# Bu çıktı, verdiğimiz komutun 0 ile 10 arası sayıları elde etmemizi sağlayacağını belirtiyor,
# ama bu sayıları o anda bize göstermiyor.!!!!!!!!!

# Daha önce verdiğimiz örneklerden de anlaşılacağı gibi, 0-10 aralığındaki sayıları görebilmek için
# range(10) ifadesi üzerinde bir for döngüsü kurmamız gerekiyor.
# range(10) ifadesinin taşıdığı sayıları görebilmek için for döngüsü kurmak tek seçenek değildir.
# Bu işlem için yıldızlı parametrelerden de yararlanabiliriz.
#  Dilerseniz şimdi bu parametre tipini range() fonksiyonuna nasıl uygulayabileceğimizi görelim:

print(*range(10),sep="/")       # (run:0/1/2/3/4/5/6/7/8/9)

# görüldüğü üzere sadece for döngüsü kullanarak değil print() fonksiyonunda * kullanarak da range() i çalıştırabiliyoruz.