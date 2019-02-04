from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Load iris dataset from sklearn
X = datasets.load_iris()

# Declare an of the KNN classifier class with the value with neighbors.
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the model with training data and target values
knn.fit(X['data'], X['target'])

# Provide data whose class labels are to be predicted

# Prints the data provided
a=int(input('type the petal length'))
b=int(input('type the petal width'))
# Store predicted class labels of X
X=[[1,2,a,b]]

prediction = knn.predict(X)

if prediction[0]==0:
    print('Setosa')
elif prediction[0]==1:
    print('Versicolor')
elif prediction[0]==1:
    print('Virginica')

#Birds of same feather flock together
