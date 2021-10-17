# Sürüme Göre İşlem Yapan Program

import sys

version2x="""
Python'un 2.x sürümlerinden birini kullanıyorsanız programı çalıştıramazsınız!
         Programı çalıştırabilmek için 3.x sürümü yükleyiniz..
"""

version3x="Programa hoşgeldiniz!"

if sys.version_info.major < 3:
    print(version2x)
else:
    print(version3x)


# sys.version_info komutu ile kullandığımız pythonun sürümünü öğrenebiliyoruz (run:sys.version_info(major=3, minor=9, micro=6, releaselevel='final', serial=0)
# bu komuta göre pythonun 3.9 sürümünü kullanıyormuşuz. major ana sürüm, minor ise ara. micro yazısı ise pythonun 3.6 ile başladığını gösteriyor 3.x serisine
# sys.version_info.minor komutu ile de minorü öğrenebiliyoruz.

# sys.version komutu da bize pythonun sürümünü veriyor aslında ama şu şekilde (run: 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)])
# eğer if den sonra sys.version u kullancak olsaydın "in" ile birlikte kullanman gerekirdi. processbyversion2 de bunu gösterdim.