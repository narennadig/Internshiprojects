import  pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import quandl
import matplotlib
from sklearn import datasets, linear_model
quandl.ApiConfig.api_key = "BWxJ2vozGo-zt4eyLcG9"
df=quandl.get('SSE/GGQ1')
df=df[['Low','High']]
X = df.values
#print(X)
df['pct']=(df['High']-df['Low'])/(df['Low'])*100
#print(df.head())



#mat = df.values
#df=df[['Low','High']]
#df['pct']=(df['High']-df['Low'])/(df['Low'])*100
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X,df['pct'])

#knn.fit(mat,df['pct'])
#c=int(input('enter the low value'))
#d=int(input('enter the high value'))
#a=[[c,d]]
#b=knn.predict(a)
#print(b)
