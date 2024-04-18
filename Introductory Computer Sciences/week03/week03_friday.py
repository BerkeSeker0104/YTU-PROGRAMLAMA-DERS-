# linspace kullanarak diziler oluştur : 
    
import numpy as np 

x = np.linspace(0, 10, 10) # linspace'de kesirli sayılar kullanıyor
print(x)

y = np.arange(0,11,1 ) # arange tam sayılar ile yapıyor bu işlemi
print(y)

z = np.arange(0,1.25,0.25 )
print(z)


yuvarlanacak_sayılar = [1.68, 99.99, -5.99, 63.65]

print(np.floor(yuvarlanacak_sayılar)) # list en alt sayıya yuvarlar
print(np.ceil(yuvarlanacak_sayılar)) # list en üst sayıya yuvarlar

'''
Herhangi birinin hipotenüs uzunluğunu hesaplayan bir program yazın. 
formülle belirtilen derecelere sahip üçgen: 
    c2=a2+b2−2AB⋅COS(θ)
    
kullanıcıdan a ve b kenar uzunluklarını iste.
ayrıca kullanıcıdan açı iste.

bunları yapan bir program yazarak hipotenüsü bulun
'''

a = int(input("Lutfen bir tam sayı kenar uzunluğu giriniz : "))
b = int(input("Lutfen bir tam sayı kenar uzunluğu giriniz : "))

ucgen_acı = int(input("Lutfen ucgen icin bir aci giriniz: "))

import math 

hipotenus_karesi= a**2+b**2-2*a*b*math.cos(ucgen_acı)
print("Ucgenimizin hipotenüsü:", math.sqrt(hipotenus_karesi))




































