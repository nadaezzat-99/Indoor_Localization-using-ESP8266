from sklearn.ensemble import RandomForestClassifier # Import Random Forest Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pandas as pd
# metrics are used to find accuracy or error
from sklearn import metrics 
from joblib import dump, load

col_names = ['STUDBME1', 'STUDBME2', 'iot', 'YME', 'Miran', 'CMP_LAB4', 'CMP_LAB2', 'label'] # CSV Header
# load dataset
data = pd.read_csv("data.csv", header=None, names=col_names,skiprows=1)

#split dataset in features and target variable
feature_cols = ['STUDBME1', 'STUDBME2', 'iot', 'YME', 'Miran', 'CMP_LAB4', 'CMP_LAB2']
X = data[feature_cols] # Features
y = data.label # Target variable

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 70% training and 30% test

# creating a RF classifier
clf = RandomForestClassifier(n_estimators = 100) 
 
# Training the model on the training dataset
# fit function is used to train the model using the training sets as parameters
clf.fit(X_train, y_train)

# performing predictions on the test dataset
y_pred = clf.predict(X_test)

# using metrics module for accuracy calculation
print("ACCURACY OF THE MODEL: ", metrics.accuracy_score(y_test, y_pred))
dump(clf, 'model.joblib')

def prediction (STUDBME1, STUDBME2, iot, YME, Miran, CMP_LAB4,CMP_LAB2):

   # create the one-dimensional array
   data = [STUDBME1, STUDBME2, iot, YME, Miran, CMP_LAB4,CMP_LAB2]
   # create the Series
   data = pd.Series(data)
   n=clf.predict([[39, 41, 36, 14,0,44,44]])
   n=clf.predict(data)
   print(n[0])
   return(n[0])