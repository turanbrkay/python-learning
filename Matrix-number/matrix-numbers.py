input("İf you want to be Matrix, press enter! ")

import random


def sayi_uret(baslangıc=0,bitis=10000000,adet=100):
    sayilar= set()

    while len(sayilar) < adet:
        sayilar.add(random.randrange(baslangıc,bitis))

    return sayilar

for i in range(999999999999999999):
    print(*sayi_uret(), sep="",end="")

