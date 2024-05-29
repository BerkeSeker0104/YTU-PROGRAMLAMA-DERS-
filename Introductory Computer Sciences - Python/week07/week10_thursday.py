import pandas as pd 

pop = pd.read_csv("C:/Users/berke/Desktop/population.csv")
print(pop)

print(pop.head())


pop_tr = pop[pop.loc[:, "CountryName"]=="Turkey"]
print(pop_tr)


movies_df = pd.read_csv("C:/Users/berke/Desktop/IMDB-Movie-Data.csv")
print(movies_df.head(10))


import matplotlib.pyplot as plt  # veri görselleştirmede kullanılır

iris = pd.read_csv("C:/Users/berke/Desktop/iris.csv", index_col=0)
print(iris)

iris.plot (x='Sepal.Length', y='Sepal.Width')
plt.show()

iris.plot(x='Sepal.Length', y='Sepal.Width', kind = "scatter")
plt.show()

iris.plot(x='Sepal.Length', y='Sepal.Width', kind = "scatter")
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title("Sepal Length vs Sepal Width")
plt.show()

