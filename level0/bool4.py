# and i çıkardığında herhangi bir sorun oluşmuyor
# burada and ve x i beraber çıkardığında, yukarıdaki komut ile aynı anlama geliyor.
# 2. ve 3. işaretli yere bak bunlar aynı şeyler

x = int(input("Notunuz: "))

if x > 100 or x < 0:
    print("Böyle bir not yok")

elif x >= 90 and x <= 100:
    print("A aldınız.")

elif x >= 80  <= 89:             #2.
    print("B aldınız.")

elif x >= 70 and x <= 79:        #3.
    print("C aldınız.")

elif 60 <= x <= 69:        # istersen 60<=x<=69 da yazabilirsin aynı anlama gelir
    print("D aldınız.")

elif x >= 0 and x <= 59:
    print("F aldınız.")

