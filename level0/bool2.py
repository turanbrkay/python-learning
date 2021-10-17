# kullanıcı adı girişinde satırı boş bıraktırmamamız gerekiyor

kullanici= input("Kullanıcı adınızı girin..")

if bool(kullanici)==True:                              # burayı "kullanici:" şeklinde kısaltabilirsin. uzun uzun yazmana gerek yok.
    print("Kullanıcı adınız onaylanmıştır!")
else:
    print("Kullanıcı adı alanı boş bırakılamaz.")