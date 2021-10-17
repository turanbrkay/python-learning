# not işleci
# değilin değili gibi bir şey

a=23
print(bool(a))                #(run:True)
print(bool(not a))            #(run:False)   burada kodun dediği: a değeri true normal de not a dediğimizde a nın değeri .... değil "false" değil
print(not a)                  #(run:False)   üstekiyle aynı anlam

b=0
print(not b)                  #(run:True)    normalde b=0 değeri False, değili ise True.

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
# gelin kolay bir kod yazalım ki mantık anlaşılsın

parola = input("parola: ")

if not parola:
    print("Parola boş bırakılamaz!")

# burada dedik ki parola değeri True değilse printi yazdır
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
input()