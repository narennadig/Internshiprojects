import pandas as pd

## Specifying column names.
#col_names = ['classe','left_weight','left_distance','right_weight','right_distance']
breast= pd.read_csv(url, header=True, names=col_names)
print(breast.head())
breast.replace('?',-9999,inplace=True)
breast_class = {'L':2,'B':4,'R':6}
breast['species_num'] = [breast_class[i] for i in breast.classe]
X = breast.drop(['classe', 'species_num'], axis=1)
y = breast.species_num
from sklearn.model_selection import train_test_split
## Split data into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)
## Import the Classifier.
from sklearn import svm
clf=svm.SVC()
clf.fit(X,y)

accuracy=clf.score(X_test,y_test)
print(accuracy*100)

## Fit the model on the training data.

# Store predicted class labels of X
L=[[2,2,3,1],[1,5,4,2],[1,4,4,1]]

prediction = clf.predict(L)
print(prediction)
