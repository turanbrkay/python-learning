# evaluate : 'değerlendirmeye tabi tutmak, işleme sokmak, işlemek’ / eval'ın açılımı
# eval tehlikeli bir fonksiyon yazılan programda çok büyük açıklar oluşturabiliyor aynı şekilde exec de.
# sistem silme komutu :  os.system('rm -rf *')      evalda bunu senin pc de yazarlarsa sıkıntı.

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print("""
*************************************************************
*              HESAP MAKİNESİ UYGULAMASI                    *
*************************************************************
TOPLAMA   +                                                 *
ÇIKARMA   -                                                 *
ÇARPMA    *                                                 *
BÖLME     /                                                 *
YAPMAK İSTEDİĞİNİZ İŞLEMİ ARADA BOŞLUK BIRAKMADAN GİRİNİZ   *
ÖRNEK İŞLEM: 23*36                                          *
 ************************************************************
""")

işlem= input("Lütfen yapmak istediğiniz işlemi giriniz...")
işlemonay= eval(işlem)

print("İŞLEMİNİZİN SONUCU:",işlemonay)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# burada eval fonksiyonu bizim işlemimizi yapmamıza imkan sağlıyor
# eğer o olmasaydı kullanıcı 23*30 girerse ekranda da 23*30 yazısını görürdük yani sayıları işleme sokmazdı.
# Kötü olan özelliği ise eğer kötü niyetli kişiler sistemi çökertmek için başka kodlar girerse onu da işleme sokuyor
# ve sistemin çökmesine neden olabiliyor o yüzden kullanırken iki kere düşünmek lazım.


# Örneğin programı çalıştırdığında işlem yapmak yerine komut satırına print("merhaba dünya") yazdığında ekrana merhaba dünya yı yazdırırsın.
# İşlem sonucu ise NONE olarak gösterilir.