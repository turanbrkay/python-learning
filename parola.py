system="Kullanıcı adı ve parolanızı toplam 20 karakteri geçmeyecek şekilde oluşturun!"
print(system)
print("*"*len(system),sep=(""))
kullanici_adi=input("Kullanıcı Adınız:")
parola=input("Parolanız:")

uzunluk= len(kullanici_adi)+len(parola)

if uzunluk > 20:
    print("Kullanıcı adınız ve parolanızın toplamı 20 karakerden fazla lütfen tekrar deneyin.. ")
else:
    print("Sisteme Hoşgeldiniz")
