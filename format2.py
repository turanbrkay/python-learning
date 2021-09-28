a="messi"
b="ronaldo"
c="firmino"
d="mane"
print("{} ve {} en sevdiğim futbolculardır.".format(a,c))                       # (run:messi ve firmino en sevdiğim futbolculardır.)

# veya

print("{} ve {} en sevdiğim aktörlerdir.".format("Al Pachino", "Tom Cruise"))   # (run:Al Pachino ve Tom Cruise en sevdiğim aktörlerdir.)

# şu şekilde de yapılabiliyor

fly= "{} jeti eskimeyen yapısıyla göz dolduruyor."
print(fly.format("f4phantom"))                                       # (run:f4phantom jeti eskimeyen yapısıyla göz dolduruyor.)

fly2="{} ve {} jetleri TSK'de aktif olarak kullanılmaktadır"
print(fly2.format("f4","f16"))                                       # (run:f4 ve f16 jetleri TSK'de aktif olarak kullanılmaktadır)