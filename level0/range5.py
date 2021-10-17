# burada range fonksiyonu kullanarak sayıları tersten yazdırmayı deneyeceğiz

for s in range(10,0,-1):
    print(s)                #(run:10,9,8,7,6,5,4,3,2,1)

# burada önemli noktalar var eğer sen parantez içindeki ilk sayıyı büyük ikinci sayıyı küçük yazarsan sonda (-) li bir sayı kullanmak zorundasın
# Yoksa çıktıda hiçbir sayı görünmez. Eğer ikişer ikişer geri yazdırmasını istiyorsan:
# (-) işareti önemli unutma!

print("*"*100)

for s2 in range(10,0,-2):
    print(s2)               #(run:10,8,6,4,2)