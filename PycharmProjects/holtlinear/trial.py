import pandas as pd
from sklearn.metrics import accuracy_score
import numpy as np
from statsmodels.tsa.holtwinters import Holt
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt

df = pd.read_csv('1.csv', nrows = 16)





fit1 = Holt(df['Count']).fit(smoothing_level=0.8, smoothing_slope=0.2, optimized=False)
fcast1 = fit1.forecast(16).rename("Holt's linear trend")




fit1.fittedvalues.plot(marker="o", color='blue',label='Holts linear trend')
#fcast1.plot(color='blue', marker="o")
plt.plot(df['Count'], label='DMA Consumption', color='red', marker="o")
plt.legend(loc='best')

plt.show()
