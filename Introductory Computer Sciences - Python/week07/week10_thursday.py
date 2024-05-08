import pandas as pd 
pop = pd.read_csv("C:/Users/berke/Desktop/Software/YTU-PROGRAMLAMA-DERSLERİ/Introductory Computer Sciences - Python\week07\population.csv")
print(pop)

print(pop.head(999)) # verileri daha iyi bir formatta gÃ¶rmek iÃ§in head() kullandÄ±k

print(pop.tail(10)) # son satÄ±rlarÄ± gÃ¶rebilmek iÃ§in tail kullandÄ±k

print(pop.info()) # veriler hakkÄ±nda bilgi alabiliriz

print(pop.describe()) # deÄiÅkenlerin her biri iÃ§in aÃ§Ä±klayÄ±cÄ± istatistikleri verir

print(pop[["CountryCode", "Total Population"]])

# yalnÄ±zca ulke koduna sahip satÄ±rlarÄ± alma 

pop_tr = pop [pop.loc[:, "CountryCode"]== "TUR"]
print(pop_tr)

# Turkiye icin yalnızca yil ve nufus degerlerini goster

print(pop_tr.loc[:,["CountryCode","Year","Total Population"]])


# IMDB movie data csv veri çerçevesini olustur
import pandas as pd

movies_df = pd.read_csv("C:/Users/berke/Desktop/Software/YTU-PROGRAMLAMA-DERSLERİ/Introductory Computer Sciences - Python\week07\IMDB-Movie-Data.csv", index_col="Title")
movies_df.head()
print(movies_df)

pd.options.display.max_columns = 99
movies_df.head()

movies_df.tail(2)