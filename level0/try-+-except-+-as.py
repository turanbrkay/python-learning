# Python bir programın çalışması esnasında hata üretirken çıktıda hata türünün adıyla birlikte kısa bir hata açıklaması veriyor
# yani hem ValueError hatası veriyor bir de yanında kısa açıklaması oluyor. örneğin:
# ValueError: invalid literal for int() with base 10: 'f'
# işte biz as kısmı ile bu kısa açıklamaya müdahale edebiliyoruz

ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except (ValueError,ZeroDivisionError) as hata:
    print(hata)                      # burada eğer kullanıcı harf veya sıfıra bölme yaparsa kısa açıklama mesajını alacak
                                     # (run:invalid literal for int() with base 10: 'öm')