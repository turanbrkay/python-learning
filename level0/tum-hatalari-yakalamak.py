# hata mesajı için:

# try:
# except ValueError:
#   print("hata!")

# böyle yapıyorduk ancak tüm hatalar için tek tek alt alta iki saat bunu mu yazacağız.
# Pythonda çıkabilecek tüm hatalar için except: yazıp alt bloğa geçerek tüm hatalara mesaj gönderebiliriz.

ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except:
    print("Bir hata oluştu!")        # burada ne hata oluşursa oluşsun hep aynı mesajı verecek
