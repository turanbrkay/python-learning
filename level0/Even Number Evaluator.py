print("""
//////////////////////////////////////////////////    
//    Çift Sayı Değerlendiriciye Hoşgeldiniz!   //
//////////////////////////////////////////////////   
   Sizden 5 tane tam sayı girmenizi isteyeceğiz
   
""")

first=int(input("İlk sayıyı giriniz:"))
second=int(input("İkinci sayıyı giriniz:"))
third=int(input("Üçüncü sayıyı giriniz:"))
fourth=int(input("Dördüncü sayıyı giriniz:"))
fifth=int(input("Beşinci sayıyı giriniz:"))


sıfırdanbuyuk = []
ciftsayılar = []

if first>=0:
    sıfırdanbuyuk += [first]
if second>=0:
    sıfırdanbuyuk += [second]
if third>=0:
    sıfırdanbuyuk += [third]
if fourth>=0:
    sıfırdanbuyuk += [fourth]
if fifth>=0:
    sıfırdanbuyuk += [fifth]



if first%2 == 0 and first>=0:
    ciftsayılar += [first]
if second%2 == 0 and second>=0:
    ciftsayılar += [second]
if third%2 == 0 and third>=0:
    ciftsayılar += [third]
if fourth%2 == 0 and fourth>=0:
    ciftsayılar += [fourth]
if fifth%2 == 0 and fifth>=0:
    ciftsayılar += [fifth]


# sum fonksiyonu ile listedikileri topluyoruz

print("Çift Sayılar:\t",ciftsayılar)
print("Listenin toplamı:\t",sum(ciftsayılar))

cifttoplam=sum(ciftsayılar)
hepsitoplam=sum(sıfırdanbuyuk)

oran= cifttoplam/hepsitoplam

print("Çift sayı oranı:\t",oran)

input()

