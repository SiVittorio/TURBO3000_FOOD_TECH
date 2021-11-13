import pandas as pd
import matplotlib.pyplot as plt

#Берет данные о дате и урожайности из файла формата .csv
df = pd.read_csv('https://raw.githubusercontent.com/SiVittorio/TURBO3000_FOOD_TECH/main/graph/data.csv')
x = df['year']
y = df['yield']

#Строит график по двум переменным
plt.bar(x, y)
plt.show()
