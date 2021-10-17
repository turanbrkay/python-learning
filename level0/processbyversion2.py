# # Sürüme Göre İşlem Yapan Program

import sys

version2x="""
Python'un 2.x sürümlerinden birini kullanıyorsanız programı çalıştıramazsınız!
         Programı çalıştırabilmek için 3.x sürümü yükleyiniz..
"""

version3x="Programa hoşgeldiniz!"

if "3.9" in sys.version:
    print(version3x)
else:
    print(version2x)