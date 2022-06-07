from sklearn.ensemble import RandomForestClassifier # Import Random Forest Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pandas as pd
# metrics are used to find accuracy or error
from sklearn import metrics 
from joblib import dump, load

{"STUDBME1", "STUDBME2", "STUDBME3", "RehabLab", "CMP_LAB1", "CMP_LAB2", "CMP_LAB3", "CMP_LAB4", "Mikasa", "Nada", "Mariem", "Alaa", "C_H_S_4", "tarek"};

col_names = ["STUDBME1", "STUDBME2", "STUDBME3", "RehabLab", "CMP_LAB1", "CMP_LAB2", "CMP_LAB3", "CMP_LAB4", "Mikasa", "Nada", "Mariem", "Alaa", "C_H_S_4", "tarek","location"] # CSV Header
# load dataset
#data = pd.read_csv("data.csv", header=None, names=col_names,skiprows=1)
data = pd.read_csv("all_data.csv", header=None, names=col_names,skiprows=1,encoding='utf-8')
print(data)

#split dataset in features and target variable
feature_cols = ["STUDBME1", "STUDBME2", "STUDBME3", "RehabLab", "CMP_LAB1", "CMP_LAB2", "CMP_LAB3", "CMP_LAB4", "Mikasa", "Nada", "Mariem", "Alaa", "C_H_S_4", "tarek"]
X = data[feature_cols] # Features
y = data.location # Target variable

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
dump(clf, 'model2.joblib')
l=clf.predict([[45, 21, 55, 19,45,38,12,45,33,44,70,45,45,38]])
print(l[0])

def prediction (StudBME1, STUDBME2, STUDBME3, RehabLab, CMP_LAB1, CMP_LAB2, CMP_LAB3, CMP_LAB4, Mikasa, Nada, Mariem, Alaa, C_H_S_4, tarek):

   # create the one-dimensional array
   data = [StudBME1, STUDBME2, STUDBME3, RehabLab, CMP_LAB1, CMP_LAB2, CMP_LAB3, CMP_LAB4, Mikasa, Nada, Mariem, Alaa, C_H_S_4, tarek]
   # create the Series
   print(data)
   data = pd.Series(data)   
   n=clf.predict(data)
   print(n)
   return(n[0])
