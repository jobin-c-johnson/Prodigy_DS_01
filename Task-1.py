import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\ASUS\Downloads\archive (4)\Population of India.csv",index_col="Sl No")
df.drop(df.index[11:36],inplace=True)
df.drop(df[df['State/UT']== 'Total (India)'].index,inplace=True)
# print(df.head(20))
bar_width = 0.35
index = range(len(df))
plt.figure(figsize=(12, 8))

plt.subplot(2,2,1)
plt.bar(index,df['Population[50]'],bar_width,color='g')
plt.title('Population Graph',pad=10)
plt.xlabel("State")
plt.ylabel('Population')
plt.xticks(index, df['State/UT'], rotation=45)

plt.subplot(2,2,2)
plt.bar(index, df['Male'], bar_width, label='Men', color='blue')
plt.bar([i + bar_width for i in index], df['Female'], bar_width, label='Women', color='pink')
plt.xlabel('States')
plt.ylabel('Male and Female Population')
plt.title('Population by State and Gender',pad=10)
plt.xticks([i + bar_width / 2 for i in index], df['State/UT'], rotation=45)

plt.subplot(2,2,3)
plt.bar(index,df['Area[52] (km2)'],bar_width,color='grey')
plt.xlabel('States')
plt.ylabel('Area')
plt.title('Area of states',pad=10)
plt.xticks(index,df['State/UT'],rotation=45)

plt.subplot(2,2,4)
plt.barh(index,df['Density (per km2)'],bar_width,color='brown')
plt.xlabel('States')
plt.ylabel('Density per Km2')
plt.title('Population density per Km2',pad=10)
plt.yticks(index,df['State/UT'])

plt.subplots_adjust(hspace=0.5)
plt.tight_layout()
plt.show()