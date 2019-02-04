

import pandas  as pd
import quandl
import math
df=quandl.get('SSE/GGQ1')
print(df.head(20))
df=df[['High','Low']]
Low='Low'
df['Low']=df[Low].shift(-1)
print(df.describe())
df['pct']=(df['High']-df['Low'])/(df['Low'])*100
df=df[['High','Low','pct']]
fore_close='Low'
df.fillna(-99999,inplace=True)
fore_out=int(math.ceil(0.01*len(df)))
df['label']=df[fore_close].shift(-fore_out)

