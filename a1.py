import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data=pd.read_csv('gapminder(2007).csv')

print(data.head())

print(data.info())

print(data.isnull().any())

sns.scatterplot(data=data,x='gdp_cap',y='life_exp')
plt.show()

sns.scatterplot(data=data,x='gdp_cap',y='life_exp',hue='continent')
plt.show()

fig, ax=plt.subplots(figsize=(8,8))

sns.scatterplot(data=data,x='gdp_cap',y='life_exp',hue='continent',size='population',sizes=(20,1000),alpha=0.7,palette='bright')
plt.show()

data =data.drop('country', axis=1)
#data =data.drop('continent', axis=1)
sns.heatmap(data.corr())
plt.show()

sns.relplot(data=data,x='gdp_cap',y='life_exp',col='continent',col_wrap=3,height=3)
plt.show()

sns.pairplot(data,hue='continent')
plt.show()