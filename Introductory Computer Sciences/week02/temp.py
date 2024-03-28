message = 'Merhabalar Python 2.hafta eğitimimize hoş geldiniz.'
print(message)

pi = 3.1415926535897932

n = 60
print(pi + n)

print(n+25)

# float kesirli sayılara denir ornek: 1.0, 15.06 gibi...

x = 3.5
print(type(x)) #type olarak float verecek

# Karmaşık sayılar 3j gibi sayılara denir 
# bunu kendimiz işlev vererek yapabiliriz ya da complex() işlevle oluşturulur.

y = 3 + 5j

print(type(y)) # type olarak complex verecek


y= complex(5.3)
print(y) 

# tam sayılar 'int'

x =10
print(type(x)) # type olarak x verecek


# bool(mantıksal) sayılar

x = True
print(type(x)) # type bool verecek

x = bool(1)
print(x)

x = bool(0)
print(x)

x = "abc"
print(x)
print(type(x))

# Slicing
my_str = "Telecommunication"

print(my_str[:5]) # ilk 5 karakteri basıtırır. 
print(my_str[5:]) # son 5 karakteri bastırır.
print(my_str[2:5])  

# List

number = [[1,2,3,4],[10,15,16,17]] # list tanımladık
print(number)

print(number[1][2])

print(number[0][1:4]) # slicing Lists

number[0][1] = 4.8 # list değiştirme 
print(number)


# List Function

number[1].append(18) # sonuna 18 ekledik
print(number)

len(number) # number list kaç elemanlı ona baktık

sayilar = [1,2,3]

sayilar.pop(1) # 2 sayısını kaldırır ve ekrana bastırır.

del sayilar[1:2] # 2 ve 3 kaldırır
print(sayilar)

x = ["a", "b", "c"] # burada x'in elemanlarını y'ye kopyaladık 
y=x
y[1] = "z" # y listesinde değişiklik yaptık
print(y)





