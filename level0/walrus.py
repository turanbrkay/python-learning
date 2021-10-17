# ":=" bunu kullanarak fazla satır yazmaktan kurtulabilirsin.
# := komutuyla "ciakimlik= len(input("CIA takma isminizi giriniz...")" cümlesini tek seferde hallettik
# (değer atama işlecidir)


if (ciakimlik := len(input("CIA takma isminizi giriniz..."))) < 10:
    print("Böyle bir takma isim olması imkansız. İp'niz alındı. ")
else:
    print("İyi çalışmalar!")

input()