import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
df = pd.read_csv('https://raw.githubusercontent.com/SiVittorio/TURBO3000_FOOD_TECH/main/graph/data.csv')
x = df['year']
y = df['yield']

#print(x)
#print(y)

plt.bar(x, y)
plt.show()
