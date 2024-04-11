import math 




# Week 2 - Questions

# Find the volume of a shpere with the radius 5 

r = 5 #yarıçap
V = 4/3*math.pi*r**3 #hacim 'V'
print('The volume of the sphere with the radius',r, 'is:',V)

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

