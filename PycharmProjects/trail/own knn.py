import matplotlib.pyplot as plt
import numpy as np
dataset={'k':[[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]]}
n_f=[5,7]
for i in dataset:
 for ii in dataset[i]:
     plt.scatter(ii[0],ii[1],s=100,color=i)
plt.scatter(n_f[0],n_f[1])
plt.show()


