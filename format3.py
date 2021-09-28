print("""
//////////////////////////////////////////////////////////
///                 KAYIT DONDURMA                     ///
///         DİLEKÇE UYGULAMASINA HOŞGELDİNİZ           ///
//////////////////////////////////////////////////////////

""")

tarih=input("Tarih:")
üni=input("Üniversite ismi:")
fakülte=input("Fakülteniz:")
bölüm=input("Bölümünüz:")
no=input("Öğrenci numaranız:")
yıl=input("Eğitim öğretim yılınız:")
dönem=input("Döneminiz:")
adsoyad=input("ad soyad:")
tc=input("TC kimlik:")
adres=input("Adres:")
tel=input("Telefon numaranız:")
ekler=input("Ekler:")

dilekce="""
                                              Tarih: {}
T.C.
{} Üniversitesi
{} Fakültesi Dekanlığına

Fakültenin {} Bölümü {} numaralı öğrencisiyim. Ekte sunduğum belgede 
belirtilen mazeretim gereğince {} Eğitim-Öğretim yılı {} yarıyılında
öğrenime ara izni istiyorum.
    Bilgilerinizi ve gereğini arz ederim.
          
    imza
          
AD-SOYAD   : {}
TC KİMLİK  : {}
ADRES      : {}
TEL        : {}
EKLER      : {}         
                                                                                        
"""
print(dilekce.format(tarih,üni, fakülte, bölüm, no, yıl, dönem, adsoyad, tc, adres,tel,ekler))

# son da yazdığımız print çok önemli print ile yazdırıken formatı bu şekilde kullanıyoruz