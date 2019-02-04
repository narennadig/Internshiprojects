import pandas as pd
import matplotlib as np
f=open("titanic.csv")
data = pd.read_csv(f,delimiter=',')
print(data.head())
