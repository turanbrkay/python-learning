# break ifadesinin temel görevi bir döngüyü sona erdirmek.
# Buradan anlayacağımız gibi, break ifadesinin her zaman bir döngü içinde yer alması gerekiyor.


while True:
    parola = input("Lütfen bir parola belirleyiniz:")
    if len(parola) < 5:
        print("Parola 5 karakterden az olmamalı!")
    else:
        print("Parolanız belirlendi!")
        break

# break olmasa program sonsuz döngüye girer