import math 




# Week 2 - Questions

# Question 1
# Find the volume of a shpere with the radius 5 

r = 5 #yarıçap
V = 4/3*math.pi*r**3 #hacim 'V'
print('The volume of the sphere with the radius',r, 'is:',V)

# Question 2
# bir kitabın fiyatı $24.95, fakat bir kitapçı satın alacaksa %40 indirim ile alıyor.
# taşıma ücreti $3. İlk kitapdan sonra her kopya için 75 cent
# 60 kopya için maliyet ne olur ?

book_price = 24.95
discount_price = 0.40
shipping_first = 3 
shipping_additional = 0.75

no_books = 60 

total_books = (book_price*(1-discount_price) )*60 + shipping_first \
        + shipping_additional*(no_books-1) 

print(total_books)

# Question 3

''' 
Matrisi oluşturmaya çalışın x=[1 0.5 0.5 1 ]
 tarafından Bu öğe gibi iç içe listeler kullanma [i],[j]
 karşılık gelen matris elemanına karşılık gelir.
'''

x = [[1, 0.5], [0.5, 1]]

print(x)
print(x[0][1])
print([1][0])

# Question 4
# Assign the matrix you just created first to x, and then assign y=x
# Change y[0][0] to 1.61 What happens to x ?

y = x
print(y)

y[0][0] = 1.61
print(y[0][0])
print(x) # x'in elemanıda değişmiş, bu python özelliğidir


# bunun olmasını istemiyorsan '.copy()' kullanıp yap.

x = [[1, 0.5], [0.5, 1]]
y = x.copy()
y[0][0] = 1.61
print(y[0][0])
print(x)

# Questions 5
# Bir cismin momentumu, kütlesinin hızıyla çarpımıdır. 
# Bir yaz Bir cismin kütlesini (kilogram cinsinden) ve hızını ( metre/saniye) 
# girdi olarak ve ardından momentumunu verir.

cismin_hızı = 10
cismin_kütlesi = 5

cismin_momentumu = cismin_hızı * cismin_kütlesi
print(cismin_momentumu)

# Questions 6 
# Hareket eden bir cismin kinetik enerjisi formülle verilir. KE=(1/2)mv2
#nerede m cismin kütlesidir ve v hızıdır. 
#Yaptığınız programı değiştirin nesnenin kinetiğini yazdıracak şekilde önceki 
# soruda oluşturulur enerji ve momentumu.


m = 8 # cismin kütlesi
v = 12 # cismin hızı
kinetik_enerji= (1/2)*m*(v**2)
print(kinetik_enerji)



# Questions 7 
# Bir çalışanın toplam haftalık ücreti, saatlik ücretin çarpımına eşittir. 
# toplam normal saat sayısı artı fazla mesai ücreti. 
# Fazla mesai ücreti toplam fazla mesai saatinin saatlik ücretin 1,5 katı ile çarpımına eşittir.
# Saatlik ücreti, toplam düzenli ücreti girdi olarak alan bir program yazın saatler 
# ve toplam fazla mesai saatleri ve bir çalışanın haftalık toplamını görüntüler ödemek.


a=45 # normal çalışma saati
b=9  # mesai saati
c=100 # saatlik ücreti 
d = a*c + b*(c*1.5)
print('haftalık toplam kazanç: ',d)

# Questions 8 
# kullanıcıdan yaşını girdi olarak isteyen bir kod yazınız.

age = int(input("Enter your age:"))
type(age)
print("I am " + str(age) + " years old.")

# Questions 9

# Aşağıdaki tabloda, dünyanın en yüksek GSYİH'sına sahip ülkeleri 2020
#ABD	21.41
#Çin	15.54
#Japonya	5.36
#Almanya	4.42
#Hindistan	3.16
#Fransa	3.06
#Birleşik Krallık	3.02
#İtalya	2.26

# yukarıdaki tabloyu kullanarak 'GDP' adlı bir list oluştur.

GDP = ['ABD', 21.41, 'Çin',	15.54, 'Japonya', 5.36,'Almanya', 4.42, \
       'Hindistan', 3.16, 'Fransa',	3.06, 'Birleşik Krallık',	3.02, \
           'İtalya',2.26]
    
print(GDP)

# liste dilimleme(slicing) kullanarak, avrupa ülkelerini seçin ve onlardan yeni GDP_Europe adlı list oluşturun

GDP_Europe = GDP[6:8] + GDP[14:16]
print(GDP_Europe)

# Turkey verisini ekle 0.81

GDP = GDP + ["Turkey", 0.81]
print(GDP)



























