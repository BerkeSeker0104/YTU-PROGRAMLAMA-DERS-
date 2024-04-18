'''
Arrays and Matrices

NumPy, sayısal analiz için temel veri türlerini sağlar – diziler ve matrisler.

Matris: Matris, iki boyutlu bir veri yapısıdır burada sayılar satırlar ve sütunlar halinde düzenlenir.

Dizi : Dizi, aşağıdakileri içeren bir veri yapısıdır: eleman grubu. Bu öğelerin türleri aynı veri türündedir
tamsayı veya dize gibi.

Bu iki veri türü arasındaki fark (Matris ve Dizi) şunlardır:

Diziler 1, 2, 3 veya daha fazla boyuta sahip olabilir ve matrisler her zaman 2 boyuta sahiptir. 
Bu, 1'e n vektörün bir dizi olarak saklandığı anlamına gelir. 1 boyut ve n öğeye sahipken, aynı vektör bir matris olarak saklanır
 boyutların boyutlarının 1 ve n olduğu 2 boyuta sahiptir ( her iki sipariş).

Dizilerdeki standart matematiksel operatörler çalışır eleman eleman. Matrisler için durum böyle değildir.

 Çarpma (*) lineer cebir kurallarına uyar. 2 boyutlu diziler "nokta" kullanılarak doğrusal cebir kuralları kullanılarak 
 çarpılabilir, ve Python 3.5 veya sonraki bir sürümü kullanılıyorsa, diziler sembolü @. Benzer şekilde, "çarpma" fonksiyonu 
 iki matris üzerinde kullanılabilir eleman eleman çarpma.

Diziler, "asmatrix" kullanılarak hızlı bir şekilde bir matris olarak ele alınabilir. veya temel verileri kopyalamadan "mat".

'''

import numpy as np 

A = np.array([[1,2,3], [4,5,6]])
print(A)

# complex dizimizi karmaşık sayı haline getiriyor 
karmaşık_sayılar = np.array([[1, 2, 3], [3, 4, 5]], dtype = complex) 
print(karmaşık_sayılar)

# '.zeros' fonksiyonu ile 0 dizisi oluşturduk
sıfır_dizisi = np.zeros((2,3))
print(sıfır_dizisi)

# .ones ile bir dizisi oluşturduk
ones_arrays = np.ones((1,5))
print(ones_arrays)



yeni_dizi=np.arange(4)
print(yeni_dizi)

# 2boyutlu dizi oluşturmak için 'reshape' kullandık.
yeni_dizi_2 = np.arange(12).reshape(2, 6)
print(yeni_dizi_2)

# len ile dizimiz kaç elemanlı bakıcaz
print(len(yeni_dizi_2))
    
np.append(yeni_dizi,10)
print(yeni_dizi)


# append ile iki diziyi birleştirdim.
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.append(x, y)
print(z)

# delete ile 1'i sildik
np.delete(x,1)
print(x)

# repeat ile 5'i 3 defa yazdırdık
print(np.repeat(5, 3))

'''
Python kodunuzda axis parametresi, np.repeat fonksiyonu ile tekrarlama işleminin 
hangi eksen boyunca yapılacağını belirler.

0: Satırları tekrarlar.
1: Sütunları tekrarlar.
'''

k = np.array([[3,5],[7,9]])
print(k)

np.repeat(k, 4, axis=0)

np.repeat(k, 4, axis=1)

'''
Matrisler esasen dizilerin bir alt kümesidir ve sanal olarak davranırlar. 
aynı şekilde. İki önemli fark şunlardır:

Matrisler her zaman 2 boyutludur

Matrisler, doğrusal cebir kurallarına uyar. Çarpma.
'''
matrix = np.array([[1, 4, 5], [-5, 8, 9]])
print(matrix)
matrix.shape # boyutunu verir.

A = np.array([[1, 4, 5,12], [-5, 8, 9, 0], [-6, 7, 11, 19]])
print("A[0] =", A[0]) # 1st row
print("A[0][0] =", A[0][0]) # 1st element of 1st row

# Matrix multiplication
# '.dot' ile iki dizinin çarpımını verir.
A = np.array([[2, 4, 0], [1, 3, 2]])
B = np.array([[3, 1, 2], [2, 3, 1], [1, 3, 3]])
A.dot(B)

# Transpose
# Transpoze işlemi, satırları sütunlara, sütunları ise satırlara dönüştürür.
A = np.array([[2, 4, 0], [1, 3, 2]])
A.transpose() #Transpose as a method


'''
Python'da np.identity() fonksiyonu, NumPy kütüphanesinde kare bir kimlik matrisi 
oluşturmak için kullanılır. Kimlik matrisi, ana çaprazındaki elemanları 1, 
diğer tüm elemanları ise 0 olan özel bir matristir.

[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''
np.identity(4)

# Inverse
# matrisin tersini almak için numpy kütüphanesinin linalg modülünü kullandık
# inv fonksiyonunu kullanarak inverse değişkenine atadık.
A = np.array([[1, 0, 2], [2, -1, 3], [4, 1, 8]])
inverse = np.linalg.inv(A)
print(inverse)


'''
numpy kütüphanesini kullanarak iki dizinin (x ve y) dikey olarak birleştirilmesini
 gerçekleştirir. Birleştirilen diziler, z adlı yeni bir diziye atanır.
 
 np.concatenate fonksiyonunu kullanarak x ve y dizilerini birleştirir.
 
 np.concatenate: İki veya daha fazla diziyi birleştirmek için kullanılan
 bir NumPy fonksiyonudur.
(x, y): Birleştirilecek dizileri içeren bir tuple.
axis=0: Dizi birleştirmenin hangi eksen boyunca yapılacağını belirtir. 
Bu durumda axis=0, dizilerin satırları boyunca birleştirme yapılacağını gösterir.
'''

x = np.array([[1 ,2],[3 ,4]])
y = np.array([[5 ,6],[7 ,8]])
z= np.concatenate((x,y),axis = 0)
print(z)


# matrisin determinatını bulmak için aşağadıki gibi yapman lazım

x = np.array([[1, 0.5], [0.5,1]])
np.linalg.det(x)


















