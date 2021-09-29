print("""
İkinci Derece Denklem Çözücü Programına Hoşgeldiniz.
Denklem için sizden a, b ve c değerlerini isteyeceğiz.              
              ax2 + bx + c = 0
""")
a=int(input("Lütfen a değerini giriniz:"))
b=int(input("Lütfen b değerini giriniz:"))
c=int(input("lütfen c değerini giriniz:"))

diskriminant= (b*b)-(4*a*c)

if diskriminant > 0:
    print("Denkleminizin 2 tane reel kökü bulundu!")
    import math
    reel1 = (-b + (math.sqrt(diskriminant))) / (2 * a)
    reel2 = (-b - (math.sqrt(diskriminant))) / (2 * a)
    print(reel1,reel2)

elif diskriminant == 0:
    print("Denkleminizin 1 tane reel kökü bulundu!")
    import math
    reel0 = (-b + (math.sqrt(diskriminant))) / (2 * a)
    print(reel0)
else:
    print("Denkleminizin reel kökü yoktur!")


input()

