import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import urllib



df2 = pd.read_csv(r'C:\Users\Philippe\Desktop\AB_NYC_2019.csv')
print(df2)
print(df2.columns)

df3 = df2['neighbourhood'].value_counts().head(10)
df3.plot(kind = 'bar')
plt.show()

df4 = sns.countplot(data= df2, x='neighbourhood_group', hue = "room_type")
plt.show()


df5 = sns.distplot(df2['price'])
plt.show()

df5 = df2[df2['price']<=500]
df6= sns.distplot(df5['price'])
plt.show()

df5.plot(
kind = 'scatter',
x = 'longitude',
y= 'latitude',
c = 'price',
cmap = 'inferno',
colorbar = True,
alpha= 0.8,
figsize=(12,8)


	)

plt.show()


#https://upload.wikimedia.org/wikipedia/commons/e/ec/Neighbourhoods_New_York_City_Map.PNG

i = urllib.request.urlopen('https://upload.wikimedia.org/wikipedia/commons/e/ec/Neighbourhoods_New_York_City_Map.PNG')
plt.imshow(plt.imread(i), zorder = 0, extent = [-74.258, -73.7, 40.49, 40.92])
ax = plt.gca()
df5.plot(
ax=ax,
zorder=1,
kind = 'scatter',
x = 'longitude',
y= 'latitude',
c = 'price',
cmap = 'inferno',
colorbar = True,
alpha= 0.8,
figsize=(12,8)
)
plt.show()