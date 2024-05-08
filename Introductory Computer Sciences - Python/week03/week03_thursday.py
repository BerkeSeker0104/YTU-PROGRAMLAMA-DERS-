# Türkiye'deki en kalabalık 5 şehrin nüfusunu içeren bir liste oluşturun Türkiye.
# Şehir isimlerini değil, sadece nüfusları kullanın.
# İstanbul 15.068 milyon
# Ankara 5.504 milyon
# İzmir 4.321 milyon
# Bursa 2.995 milyon
# Antalya 2.426 milyon

pop = [15.068, 5.504, 4.321, 2.995, 2.426]

print(max(pop)) # listedeki max değeri gösterecek
print(min(pop)) # listedeki min değeri gösterecek

print(round(15.068, 2)) # değeri yuvarlamamıza yarıyor. 2 yazdık çünkü 2 basamak yuvarlamak istedik.

help(round) # round fonksiyonun işlevini gösterir 

pop_inc = sorted(pop) # küçükten büyüğe sıralayacak
print(pop_inc)

pop_decr = sorted(pop, reverse=True) # büyükten küçüğe sıralayacak
# reverse=True ile sorted fonksiyonunun tersini yapacak.
print(pop_decr)

print(len(pop)) # list eleman sayisini verir.

print(sum(pop)) # listedeki elemanların toplamını verir.

''' 
numPy Python programalama dilinde büyük, çok boyutlu dizileri ve matrisleri 
destekleyen ve bu diziler üstünde çalışabilecek üst düzey matematiksel 
işlevler ekleyen bir kütüphanedir.

bu kütüphaneyi kullanabilmek için:
    import numpy as np
'''

import numpy as np

'''
.array fonksiyonu n boyutlu dizileri oluşturmak için kullanılır.
'''

dizi = np.array([1,2,3]) 
print(dizi)

#prod() fonksiyonu, 
#Python'da bir iterable nesnesinin elemanlarının çarpımını hesaplamak için kullanışlı bir araçtır.

print(np.prod(pop)) # listedeki çarpımları verir.

'''
Python'da linspace() fonksiyonu, belli bir aralıktaki sayıları eşit aralıklarla
oluşturmak için kullanılır. Bu fonksiyon, numpy kütüphanesi ile gelir.
üç argüman alır: 
    
    start: aralığın başlangıç noktası
    stop: aralığın bitiş noktası
    num: oluşturalacak sayının adedi
    
# 0'dan 10'a kadar 5 eşit aralıklı sayı oluşturma
dizi = np.linspace(0, 10, 5)
print(dizi)  # [0.  2.5  5.  7.5 10. ] yazdırır

'''

x = np.linspace(0,10,10)
print(x)

'''
Python'da arange() fonksiyonu, 
belirli bir aralıktaki sayıları eşit aralıklarla veya belirli bir adımla oluşturmak 
için kullanılır. 

Bu fonksiyon, numpy kütüphanesinden gelir ve üç argüman alabilir:

start: Aralığın başlangıç noktası.
stop: Aralığın bitiş noktası.
step: Oluşturulacak sayılar arasındaki adım.


# 5'ten 15'e kadar 2'şer 2'şer artan sayıları oluşturma
dizi = np.arange(5, 15, 2)
print(dizi)  # [ 5  7  9 11 13] yazdırır


'''

# 0'dan 25'e 0,5 artışla artan bir dizi oluşturun. en son hepsini toplayın.

dizi = np.arange(0,25.5,0.5) #25.5 yaptım çünkü 25 de bitmesini istiyorum ondan dolayı
print(dizi)

print(sum(dizi)) # dizinin elemanlarının toplamını verir.

'''
randn() fonksiyonu, standart normal dağılımdan rastgele sayılar üretir.
numpy kütüphanesinde bulunur.
'''

rando_number = np.random.randn(10)
print(rando_number)


'''
floor() fonksiyonu bir sayıyı en yakın alt tam sayıya yuvarlar.
ceil() fonksiyonu bir sayıyı en yakın üst tam sayıya yuvarlar.

iki fonksiyonda pozitif ve negatif sayılar için kullanılabilir.
sonuç her zaman tam sayı çıkar.

'''
print(np.floor(rando_number)) 
print(np.ceil(rando_number))

print(rando_number)

'''
exp() fonksiyonunun özellikleri:

Bir sayıyı argüman olarak alır ve e sayısının bu sayıya göre üssünü döndürür.
math modülünden çağrılması gerekir.
e sayısı, yaklaşık 2.7182818 değerine sahip
Sonuç her zaman bir reel sayıdır.
Negatif üsler için de kullanılabilir, ancak sonuç karmaşık bir sayı olabilir.

pow() fonksiyonunu kullanabilirsiniz. Ancak, pow() fonksiyonu sadece tam sayı 
üsler için tam olarak doğrudur.
'''

print(np.exp(rando_number))


'''
Python'da log() fonksiyonu, bir sayının (x) temel bir sayıya (b) göre logaritmasını 
hesaplamak için kullanılır. Logaritma, bir sayının temel bir sayıya kaç defa 
çarpılması gerektiğini bulma işlemidir.

import math

# 10 tabanında logaritma
x = 100
onluk_logaritma = math.log(x)
print(onluk_logaritma)  # 2.0 yazdırır

# e tabanında logaritma (doğal logaritma)
e_tabanli_logaritma = math.log(x, math.e)
print(e_tabanli_logaritma)  # 4.605170918075868 yazdırır

# 2 tabanında logaritma
iki_tabanli_logaritma = math.log2(x)
print(iki_tabanli_logaritma)  # 6.643856197347606 yazdırır
'''

print(np.log(rando_number))
print(np.log10(rando_number))

'''
Python'da sqrt(x) fonksiyonu, bir sayının karekökünü hesaplamak için kullanılır. 
Karekök, bir sayıyı kendisiyle çarparak elde edilen sayıdır.


'''

print(np.sqrt(rando_number))


'''
Python'da numpy kütüphanesindeki abs() fonksiyonu, bir sayının mutlak değerini 
hesaplamak için kullanılır. Mutlak değer, bir sayının pozitif veya negatif 
olmasına bakılmaksızın büyüklüğünü temsil eder.
'''

print(np.abs(rando_number))


'''
Python'da numpy kütüphanesinin sign() fonksiyonu, bir veya birden fazla boyutlu 
dizi elemanlarının işaretlerini element bazında hesaplamak için kullanılır.
Bu işaretler, elemanın pozitif, negatif veya sıfır olup olmadığını gösteren 
-1, 0, 1 değerlerinden oluşur.
'''
print(np.sign(rando_number))



# list methods

crowded = ["Istanbul", 15.068, "Ankara", 5.504, "Izmir", 4.321, "Bursa", 2.995, "Antalya", 2.426]
print(crowded)

print(crowded.index("Istanbul")) #listdeki konumunu veriyor bize 0 yani ilk eleman

print(crowded.index("Ankara"))

'''
Python'da "Calculating a count" (count) ifadesi, bir dizideki veya 
stringdeki belirli bir ögenin (elemanın) kaç kez tekrarladığını bulmak anlamına gelir.
'''

score = [3, 3, 1, 1, 0, 3, 1, 1, 0, 3]

print(score.count(3)) # 3 kaç kez tekrarlanmış onu söyler



text = "python is SO cool!"

print(text.lower()) # string metnin hepsini küçük harfe çevirir.
print(text.upper()) # string metnin hepsini büyük harfe çevirir.

# Python'da capitalize() fonksiyonu, bir stringin (karakter dizisinin) ilk 
# harfini büyük harfe çevirir ve geri kalan harfleri küçük harfe bırakır.

print(text.capitalize())

print(text.title()) # her kelimenin baş harfini büyük yapar.


print(text.replace("SO", "very")) # string halde olan metinden silme işlemi yapar.
# list de silme işlemi yapamaz.



# append() list' eleman eklememize yarıyor.
crowded.append("Adana") 
crowded.append(2.220)
print(crowded)


































 
