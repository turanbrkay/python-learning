# kullanıcıdan aldığımız harf ile metinde ne kadar o harften geçiyor onu bulacağız


genclik="""
   Ey Türk gençliği! Birinci vazifen; Türk istiklalini, Türk cumhuriyetini, ilelebet muhafaza ve müdafaa etmektir.

   Mevcudiyetinin ve istikbalinin yegâne temeli budur. Bu temel, senin en kıymetli hazinendir.
   İstikbalde dahi seni bu hazineden mahrum etmek isteyecek dâhilî ve haricî bedhahların olacaktır. 
   Bir gün, istiklal ve cumhuriyeti müdafaa mecburiyetine düşersen, vazifeye atılmak için içinde bulunacağın vaziyetin imkân ve şeraitini düşünmeyeceksin.
   Bu imkân ve şerait, çok namüsait bir mahiyette tezahür edebilir. 
   İstiklal ve cumhuriyetine kastedecek düşmanlar, bütün dünyada emsali görülmemiş bir galibiyetin mümessili olabilirler. 
   Cebren ve hile ile aziz vatanın bütün kaleleri zapt edilmiş, bütün tersanelerine girilmiş, bütün orduları dağıtılmış ve memleketin her köşesi bilfiil işgal edilmiş olabilir. 
   Bütün bu şeraitten daha elim ve daha vahim olmak üzere, memleketin dâhilinde iktidara sahip olanlar, gaflet ve dalalet ve hatta hıyanet içinde bulunabilirler. 
   Hatta bu iktidar sahipleri, şahsi menfaatlerini müstevlilerin siyasi emelleriyle tevhit edebilirler. Millet, fakruzaruret içinde harap ve bitap düşmüş olabilir.

   Ey Türk istikbalinin evladı! İşte, bu ahval ve şerait içinde dahi vazifen, Türk istiklal ve cumhuriyetini kurtarmaktır. 
   Muhtaç olduğun kudret, damarlarındaki asil kanda mevcuttur.

  Mustafa Kemal Atatürk
"""
izinlikarakterler="abcdefgğhıijklmnoöprsştuüvyz"
harf=input("Bir harf girin...")
sayi= 0


for a in genclik:        # burada her a sayisi gördüğünde sayi=0 değerini bir artırıyor
    if a == harf:
        sayi += 1


for k in harf:                             # burada eğerki kullanıcı alfabeden başka bir şey girmeye çalışırsa ona izin vermiyoruz. continue ile de alttaki printi geçiyoruz
    if k not in izinlikarakterler:
        print("Lütfen Türkçe harf giriniz..")
        continue


    print("Metinde Bulunan {} harfi sayisi: ".format(harf),sayi)

input()
