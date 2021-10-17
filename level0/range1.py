# belirli aralıktaki sayıları göstermek için kullanılır range()

for sayi in range(0,10):
    print(sayi)

# çıktımız 0,1,2,3,4,5,6,7,8,9 dur. 10'u almadı. Son sayının dahil olmadığını bilmelisin. İlk sayıyı alır, son sayıyı almaz.

print("/"*100)

for sayi2 in range(10):
    print(sayi2)

# burada ise eğer ki ilk sayının sıfırdan başlamasını istiyorsan sıfır yazıp virgül koymana gerek yok.
# Direkt hangi sayıya kadar çıktı almak istiyorsan onu yazabilirsin. Belirtilmediğinde çıktı sıfırdan başlar