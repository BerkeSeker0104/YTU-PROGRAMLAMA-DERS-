'''
Boolean Expressions

aritmatik ifadeler sayısal değerlere göre değerlendirilir.
Bool ifadeleri True ve False'tur.
'''

print(True)

print(False)

# if - elif - else

'''
Python'da if ve else olmak üzere iki temel koşul ifadesi bulunur. Bunlar,
programın belirli koşullara bağlı olarak farklı kod bloklarını çalıştırmasını sağlar.

Karmaşık koşullarda if ve else ile birlikte elif (else if) ifadeleri kullanılabilir. 
elif ile birden fazla koşul kontrol edilebilir.

if koşullarında birden fazla koşulu birleştirmek için and (ve), or (veya) ve 
not (değil) gibi mantıksal operatörler kullanılabilir.

'''

# Example 1. Let us write a program that asks you the password and check if it is True

password = input("Enter the password: ")

if password == "prospero":
     print('Password accept.')
else:
    print('Password error.')
    
# Example 2 In this program, let us check if the number is positive or negative or zero and display an appropriate message  
    
number = float(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")
    
    
    
# Example 3
value = eval(input("Please enter an integer in the range 0...5: "))
if value < 0:
    print("Too small")
else:
    if value == 0:
        print("zero")
    else:
        if value == 1:
            print("one")
        else:
            if value == 2:
                print("two")
            else:
                if value == 3:
                    print("three")
                else:
                    if value == 4:
                        print("four")
                    else:
                        if value == 5:
                            print("five")
                        else:
                            print("Too large")
print("Done")


'''
for Statements

Python'da for döngüsü, tekrarlayan işlemleri gerçekleştirmek için kullanılan temel bir döngü türüdür. 
Belirli bir kod bloğunun bir dizi veya koleksiyon üzerindeki her öğe için tekrarlanmasını sağlar.

'''

courses = ["Sampling", "Applied Statistics", "Robust Statistics"]
for i in courses:
    print(i, len(i))
    
# break ile döngüyü direkt durdurabiliriz.

courses = ["Sampling", "Applied Statistics", "Robust Statistics"]
for i in courses:
    print(i)
    if i== "Applied Statistics":
        break # Robust Statistics bu kısım döngüye girmeyecek 
        
        
# continue Statements ile istediğimiz kısmı atlayarak döngüye devam edecektir.

courses = ["Sampling", "Applied Statistics", "Robust Statistics"]
for i in courses:
    if i== "Applied Statistics":
        continue
    print(i)    
    
    
    
# range() fonksiyonu belli bir aralıktaki sayıları üretmek için kullanılır.

for x in range (2, 6):
    print(x)


for y in range (0, 30, 3):
    print(y)
else:
  print("Finally finished!")


'''
While Sttatments

Python'da while döngüsü, belirli bir koşul sağlandığı sürece kod bloğunun tekrar tekrar çalıştırılmasını sağlayan 
bir döngü türüdür. Koşul False (yanlış) hale gelene kadar döngü devam eder.

while Döngüsü Kullanım Alanları:

Kullanıcıdan veri girişi alınması gibi etkileşimli işlemler için kullanılabilir.
Dosyaları satır satır okuma gibi tekrarlayan görevler için kullanılabilir.
Bir işlemin tamamlanmasını bekleme gibi bekleme durumları için kullanılabilir.


'''

# Print i as long as i is less than 6:
    
i = 1 

while i<=6:
    print(i)
    i+=1
    
    
    
    
















