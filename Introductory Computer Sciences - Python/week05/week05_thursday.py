'''
Python'da dictionary (sözlük), verileri anahtar-değer çiftleri halinde depolayan bir veri yapısıdır. 
Eğer bir gerçek sözlüğü düşünürseniz, kelimeler anahtar görevi görür ve tanımları değer görevi görür.

Sözlük öğeleri belli sıra halinde değillerdir. 
farklı veri türlerinde olabilirler.
keywordslar değiştirilemezler fakat değerleri değiştirilebilir.
'''

city_pop = {"Istanbul": 15.068, "Ankara":5.504, "Izmir":4.321, "Bursa":2.995, "Antalya":2.426}
print(city_pop)
print(city_pop["Istanbul"]) 

city_pop["Adana"] = 2.1 # dictionarye böyle eleman ekliyoruz.
print(city_pop)

del city_pop["Bursa"] # dictionarye da böyle eleman siliyoruz
print(city_pop)

print(city_pop.keys()) # bununla sadece keywordsları bastırabilirsin
print(city_pop.values()) # bununla sadece değerleri bastırabilirsin

# From string in countries and capitals, create dictionary europe
europe = { 'spain':'madrid', "france":"paris", "germany":"berlin","norway":"oslo" }

# Print europe
print(europe)

# list ile bir dictionary oluşturabiliriz 
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

europe2 = dict(zip(countries, capitals))
print(europe2)

# dictionary ile daha karmaşık listler oluşturabiliriz. Aşağıdaki gibi:
# Dictionary of dictionaries
europe_3 = { 'spain': { 
            'capital':'madrid', 
            'population':46.77 
          },
           'france': { 
           'capital':'paris', 
           'population':66.03 
          },
           'germany': { 
           'capital':'berlin', 
            'population':80.62 
          },
           'norway': { 
           'capital':'oslo', 
           'population':5.084 
           },
           'turkey': {
           'capital':'ankara', 
           'population':80.81
           }
}

print(europe_3)

print(europe_3["france"])

'''
Pandas, python programlama dilinde veri analizi için kullanılan güçlü bir kütüphanedir.
Özellikle tablo benzeri verileri işlemek için tasarlanmıştır.

Veri Yapıları: Pandas, iki ana veri yapısı sunar:
Seriler: Tek bir veri tipinden oluşan tek boyutlu dizilerdir. Zamana bağlı verileri (örneğin hisse senedi fiyatları) 
temsil etmek için idealdir.
Veri Çerçeveleri: İki boyutlu tablolardır. Satırlar ve sütunlardan oluşurlar ve her sütun farklı bir veri türüne sahip olabilir.
 Veri Çerçeveleri, ilişkisel verileri (örneğin müşteri bilgileri) depolamak için idealdir.
Veri İşleme ve Analizi: Pandas, verileri filtrelemek, sıralamak, gruplamak, birleştirmek ve agrega etmek için çeşitli 
işlevler sunar. Ayrıca veri görselleştirme, istatistiksel hesaplamalar ve makine öğrenimi modelleri oluşturma gibi görevler 
için de kullanılabilir.

Pandas'ın Kullanım Alanları:

Veri Temizleme ve Hazırlama: Eksik verileri ele alma, tutarsızlıkları düzeltme ve verileri analiz için uygun bir formata 
dönüştürme gibi görevler için kullanılabilir.

Veri Analizi: Verileri keşfetmek, istatistiksel özetler oluşturmak, trendleri belirlemek ve tahminler yapmak için kullanılabilir.
Makine Öğrenmesi: Verileri makine öğrenimi modellerini eğitmek için hazırlamak ve model performansını değerlendirmek için 
kullanılabilir.

Finansal Analiz: Hisse senedi fiyatları, döviz kurları ve diğer finansal verileri analiz etmek için kullanılabilir.

Pazarlama Analizi: Müşteri davranışlarını analiz etmek, pazarlama kampanyalarının etkinliğini değerlendirmek ve müşteri 
segmentleri oluşturmak için kullanılabilir.


'''


# Creating a pandas dataframe from a set of lists and dictionaries

# To create a data frame from a set of dictionaries, data should be kept slightlhy different in dictionaries.
# Each variable should be contained in a different list.
Sepal_Length = [5.1, 4.9, 4.7, 4.6, 7.0, 6.4, 6.9, 5.5, 6.3, 5.8, 7.1, 6.3]
Sepal_Width = [3.5, 3.0, 3.2, 3.1, 3.2, 3.2, 3.1, 2.3, 3.3, 2.7, 3.0, 2.9]
Species = ["setosa", "setosa", "setosa", "setosa", "versicolor", "versicolor", "versicolor", "versicolor",
"virginica", "virginica", "virginica", "virginica"]

iris = {"Sepal.Length":Sepal_Length, "Sepal_Width": Sepal_Width, "Species": Species}

# Import as and turn the dictionary into a data frame with the function.pandaspdDataFrame()

import pandas as pd

iris_df = pd.DataFrame(iris) # bu kod iris veri kümesini yüklemek için ve pandas veri çerçevesi oluşturmak için kullanılır.
print(iris_df)

# ismi rowname yapmak istersen : 

iris_df.index = ["flower" + str(i) for i in range(1,13)]
print(iris_df)

# Creating a dataframe from a csv file

import pandas as pd
iris_df_new = pd.read_csv("C:/Users/berke/Desktop/Software/YTU-PROGRAMLAMA-DERSLERİ/Introductory Computer Sciences - Python\week05\iris.csv")
print(iris_df_new)

'''
iris_df = pd.read_csv("iris.csv", index_col=0) kodunda yer alan index_col parametresi, 
pd.read_csv() fonksiyonunun veri okurken hangi sütunun veri çerçevesinin indeksi olarak 
kullanılacağını belirlemenizi sağlar.
'''

# Sepal.Length keywordsunu çalıştırmak için kullanılır.
print(iris_df_new[["Sepal.Length"]]) 

#Selecting Rows

print(iris_df_new[24:30])

# Row access with loc() 
# satır etkiketlerini çağırmak için kullanılır 

print(iris_df_new.loc[10])


'''
.loc: Etiket tabanlı erişim sağlar. Bu, satır ve sütun adlarını veya label'ları kullanarak veri erişimi anlamına gelir. 
.loc ile hem satırları hem de sütunları seçebilirsiniz.

.iloc: Pozisyon tabanlı erişim sağlar. Bu, satır ve sütun numaraları kullanarak veri erişimi anlamına gelir. 
.iloc ile genellikle sadece satırları seçersiniz, sütunları seçmek için genellikle .iloc ile birlikte boole dizileri kullanılır.
'''

print(iris_df_new.loc[[10]])





























