# continue deyiminin görevi kendisinden sonra gelen her şeyin es geçilip döngünün başına dönülmesini sağlamaktır.

while True:
    s = input("Döngüden çıkmak için 'iptal' yazabilirsiniz.\nBir sayı girin: ")
    if s == "iptal":
        break

    if len(s) <= 3:
        continue

    print("En fazla üç haneli bir sayı girebilirsiniz.")

# burada eğer 3 haneden az bir sayı girerseniz döngü alttaki print fonksiyonunu yazdırmadan direkt başa döner.