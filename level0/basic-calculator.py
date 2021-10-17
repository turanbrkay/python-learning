print("""
//////////////////////////////////  
//  Hesap Makinesi Uygulaması   //
//////////////////////////////////
//   (1) Toplama                //    
//   (2) Çıkarma                //
//   (3) Çarpma                 //
//   (4) Bölme                  //
//   (5) Karesini Hesapla       //
//   (6) Karekök Hesapla        //
//////////////////////////////////              

""")

islem= input("Yapmak istediğiniz işlemin numarasını giriniz...")

if islem=="1":
    sayi1=int(input("İlk sayıyı giriniz..."))
    sayi2=int(input("İkinci sayıyı giriniz..."))
    print("İşleminizin sonucu:", sayi1+sayi2)

elif islem=="2":
    sayi11=int(input("İlk sayıyı giriniz..."))
    sayi22=int(input("İkinci sayıyı giriniz..."))
    print("İşleminizin sonucu:", sayi11-sayi22)

elif islem=="3":
    sayi111=int(input("İlk sayıyı giriniz..."))
    sayi222=int(input("İkinci sayıyı giriniz..."))
    print("İşleminizin sonucu:", sayi111*sayi222)

elif islem=="4":
    sayi1111=int(input("İlk sayıyı giriniz..."))
    sayi2222=int(input("İkinci sayıyı giriniz..."))
    print("İşleminizin sonucu:", sayi1111/sayi2222)

elif islem=="5":
    sayi15=int(input("Karesini hesaplamak istediğiniz sayıyı girin..."))
    print("İşleminizin sonucu:", sayi15**2)

elif islem=="6":
    sayi16=int(input("Karekökünü almak istediğiniz sayıyı girin..."))
    print("İşleminizin sonucu:", sayi16**0.5)
else:
    print("Geçersiz işlem..")

input()