# pass i kullanarak "boşver, geç" diyoruz aslında örneğin:

while True:
    parola = input("parola belirleyin: ")

    if not parola:
        pass                  # burada pass i kullanarak pythona dedik ki eğer kullanıcı parola girmemişse boşver sen devam et programı okumaya.
                              # bu yüzden kullanıcının karşısına sürekli parola belirleyin yazısı çıkacak

    elif len(parola) in range(3, 8): #eğer parolanın uzunluğu 3 ile 8 karakter
        #aralığında ise...
        print("Yeni parolanız", parola)
        break

    else:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")