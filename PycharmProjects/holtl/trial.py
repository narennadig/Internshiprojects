
from statsmodels.tsa.holtwinters import  Holt
import pandas as pd
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv('1.csv',
                 parse_dates=['Month'],
                 index_col='Month'
)
df.index.freq = 'MS'
train, test = df.iloc[:12, 0], df.iloc[11:, 0]




y_hat_avg = test.copy()
print(train[''])

fit1 = Holt(np.asarray(train)).fit(smoothing_level = 0.3,smoothing_slope = 0.1)
y_hat_avg['Holt_linear'] = fit1.forecast(len(test))

plt.figure(figsize=(16,8))
plt.plot(train, label='Train')
plt.plot(test, label='Test')
plt.plot(y_hat_avg, label='Holt_linear')
plt.legend(loc='best')
plt.show()

