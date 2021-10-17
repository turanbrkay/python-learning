# Amacımız dosya içerisinde bulunan iki .txt dosyalarındaki takımların içeriğini karşılaştırıp, aynı öğeleri ortaya sermek.

t1=open("evsahibi.txt")          # dosyayı açıyoruz
t1_satır = t1.readlines()        # satırları okuyoruz

t2=open("deplasman.txt")
t2_satır = t2.readlines()

for karsılastırma in t1_satır:
    if karsılastırma in t2_satır:
        print(karsılastırma)

t1.close()
t2.close()
