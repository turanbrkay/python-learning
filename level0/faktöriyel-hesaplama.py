sayi = int(input("Faktöriyelini almak istediğiniz sayıyı girin..."))

a=1
for i in range(1,sayi+1):
    a = a*i
    


print("{}! = ".format(sayi),a)