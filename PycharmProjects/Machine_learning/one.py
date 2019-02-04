
import numpy as np
import pandas as pd

data = pd.read_csv("Users/Apple/desktop/1.csv", index_col=False, header=0)
x = data.Month.values
y = data.Consumption.values
print(x)
