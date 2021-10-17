# metin içinde bazı harfler birden fazla sayıda geçtiği için, doğal olarak çıktıda da bu harfler birden fazla sayıda görünüyor.
# Ama tabii ki, eğer biz istersek farklı olan her harften yalnızca bir tanesini çıktıda görmeyi de tercih edebiliriz.
# Bunun için şöyle bir kod yazabiliriz:


ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

fark = ""

for s in ikinci_metin:           # ikinci_metin'de 's' dediğimiz bütün öğeler için
    if not s in ilk_metin:       # eğer 's' ilk_metin'de yoksa
        if not s in fark:        # eğer 's' fark'ta da yoksa
            fark += s            # bu öğeyi fark değişkenine ekle
print(fark)                      # fark değişkenini ekrana bas

# fark adlı boş bir karakter dizisi tanımlıyoruz.
# Metinler içindeki farklı karakter dizilerini fark adlı bu karakter dizisi içinde depolayacağız.