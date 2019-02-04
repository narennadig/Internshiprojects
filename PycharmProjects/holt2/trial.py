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
model = ExponentialSmoothing(train, seasonal='mul', seasonal_periods=12).fit()
pred = model.predict(start=test.index[0], end=test.index[-1])

print accuracy_score(test, pred)
print(accuracy_score(test, pred, normalize=False))
plt.plot(train.index, train, label='Train')
plt.plot(test.index, test, label='Test')
plt.plot(pred.index, pred, label='Holt-Winters')
plt.legend(loc='best')
plt.show()



rms = sqrt(mean_squared_error(test.Count, y_hat_avg.Holt_Winter))
print(rms)
