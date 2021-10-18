# finally.. bloğunun en önemli özelliği, programın çalışması sırasında herhangi bir hata gerçekleşse de gerçekleşmese de işletilecek olmasıdır.
# Eğer yazdığınız programda mutlaka ama mutlaka işletilmesi gereken bir kısım varsa, o kısmı finally... bloğu içine yazabilirsiniz.
# finally... bloğu özellikle dosya işlemlerinde işimize yarayabilir.

try:
    dosya = open("dosyaadı", "r")
    #...burada dosyayla bazı işlemler yapıyoruz...
    #...ve ansızın bir hata oluşuyor...
except IOError:
    print("bir hata oluştu!")
finally:
    dosya.close()

# Burada finally... bloğu içine yazdığımız dosya.close() ifadesi dosyamızı güvenli bir şekilde kapatmaya yarıyor.
# Bu blok, yazdığımız program hata verse de vermese de işletilecektir.