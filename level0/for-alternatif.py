tanım = "Atatürk, Türkiye Cumhuriyeti Devleti'nin kurucusudur."

for karakter in tanım:
    print(karakter)

# bu işlemi for la yapmaktansa print ile kısaca yapabilirsin

print(*tanım)         # ( run:  A t a t ü r k ,   T ü r k i y e   C u m h u r i y e t i   D e v l e t i ' n i n   k u r u c u s u d u r . )
# yanına virgül atıp sep parametresini yazdığında ise for döngüsüyle aynı işlemi yapmış oluyor.

print(*tanım, sep="\n")