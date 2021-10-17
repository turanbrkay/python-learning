# range fonksiyonu 3 tane de değer alabilir yani (0,10,2) gibi
# bu üçüncü değer atlama aralığıdır yani 0 ile 10 arasını kaçar kaçar yazdıracağımızı belirtir

for sayi in range(1,10,2):
    print(sayi)

# (run:1,3,5,7,9) 1 den başladı ve ikişer ikişer atlayarak dokuza kadar gitti.
# Eğer atlama aralığını kullanmak istiyorsak range fonskiyonundaki üç parametreyide yazman gerekiyor. (-,-,-) yoksa kullanamazsın