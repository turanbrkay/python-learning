# bool işleçlerinden "and" i burada kullandık
print("""

//////////////////////////////////////////////////////////////////
//   Kullanıcı adı ve şifre oluşturma programına hoş geldiniz!  //
//////////////////////////////////////////////////////////////////
//  Oluşturacağınız kullanici adı ve şifre 6 karakterden büyük  //
//             15 karakterden küçük olmalıdır                   //    
//////////////////////////////////////////////////////////////////

""")
kullaniciadi= input("Kullanıcı adı giriniz...")
sifre= input("Şifrenizi giriniz...")

uzunluksifre= int(len(sifre))
uzunlukkullanici= int(len(kullaniciadi))

if  15>uzunluksifre>6 and 15>uzunlukkullanici>6:
    print("Tebrikler! Hesabınız oluşturuldu.")
else:
    print("Kullanıcı adı ve şifre girme işlemini yanlış yaptınız! Tekrar deneyin.")

input()

