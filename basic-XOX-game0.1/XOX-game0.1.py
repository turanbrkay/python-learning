# XOX - OYUNU
print("""
    BASİT XOX OYUNUNA HOŞGELDİNİZ
OYUNU İLK ÜÇLEMEYİ YAPAN KAZANACAKTIR\n\n
""")

tahta= [["___","___","___","___"],
        ["___","___","___","___"],
        ["___","___","___","___"],
        ["___","___","___","___"]]


     # tahta için ekranda boş bir alan oluşturduk

for i in tahta:
        print("\t".expandtabs(30), *i, end="\n"*2)     # bu işlem ile tahtamızı ekranda ortaya taşıdık ve sadeleştirdik. (*i ile sadeleştirdik)


kazanmadurumu=[[[0,0],[0,1],[0,2]],
               [[0,1],[0,2],[0,3]],
               [[1,0],[1,1],[1,2]],
               [[1,1],[1,2],[1,3]],
               [[2,0],[2,1],[2,2]],
               [[2,1],[2,2],[2,3]],
               [[3,0],[3,1],[3,2]],
               [[3,1],[3,2],[3,3]],
               [[0,0],[1,0],[2,0]],
               [[1,0],[2,0],[3,0]],
               [[0,1],[1,1],[2,1]],
               [[1,1],[2,1],[3,1]],
               [[0,2],[1,2],[2,2]],
               [[1,2],[2,2],[3,2]],
               [[0,3],[1,3],[2,3]],
               [[1,3],[2,3],[3,3]],
               [[0,0],[1,1],[2,2]],
               [[1,1],[2,2],[3,3]],
               [[0,1],[1,2],[2,3]],
               [[1,0],[2,1],[3,2]],
               [[2,0],[1,1],[0,2]],
               [[3,0],[2,1],[1,2]],
               [[2,1],[1,2],[0,3]],
               [[3,1],[2,2],[1,3]]]        # koordinat üzerinde kazanma ölçütlerini bildirdik.


x_durum= []
o_durum= []          # x ve o nun oyun içindeki konumlarını bellekte tutmak için listesini oluşturduk


# sırayla oynanması için şunları yazıyoruz

sıra= 0

while True:
    if sıra%2 == 0:
            harf = "X".center(3)                  # buradaki center, X i, "___" buradaki yerinde ortalıyor. 3 tane ___ olduğu için paranteze 3 yazdık.
    else:
            harf = "O".center(3)

    print()
    print("SIRA: {}".format(harf))


    y = input("Soldan Sağa [1,2,3,4]".ljust(30))
    if y == "q":
        break

    x = input("Yukarıdan Aşşağı [1,2,3,4]".ljust(30))            # burada kullanıcıdan koordinatları girmesini istiyoruz
    if x == "q":
            break



    print("\n")
    x=int(x)-1
    y=int(y)-1      # python koordinatlara 0 dan başlıyor ama biz kullanıcıya 1 ile başlamasını söyledik yukarıda, bunu düzeltmek için bu kodu yazdık

    if tahta[x][y]=="___":
        tahta[x][y] = harf
        if harf == "X".center(3):
            x_durum += [[x, y]]
        elif harf == "O".center(3):
            o_durum += [[x, y]]
        sıra += 1
    else:
        print("\n Girdiğiniz Konum Dolu, Tekrar Girin..\n")

    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n"*2)


    for i in kazanmadurumu:
        o = 0
        for z in i:
            if z in o_durum:
                o += 1

        x = 0
        for z in i:
            if z in x_durum:
                x += 1

       # for i in kazanmadurumu:
        #    o = [z for z in i if z in o_durum]
         #   x = [z for z in i if z in x_durum]



            if o == 3:
                for i in tahta:
                    print("O KAZANDI!")
                    input("TEBRİKLER")
                    quit()
            if x == 3:
                for i in tahta:
                    print("X KAZANDI!")
                    input("TEBRİKLER")
                    quit()






