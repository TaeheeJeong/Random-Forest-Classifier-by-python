# Random Forest classifer

"""
Created on Mon May 09 16:37:35 2016

@author: Taehee Jeong
"""
import pandas as pd

#%%Load the dataset

AH_data = pd.read_csv("C:/Bigdata/Machine learning for Data Analysis/wk1/tree_addhealth.csv")

data_clean = AH_data.dropna()

data_clean.dtypes
data_clean.describe()

# features and target


all_features = ['BIO_SEX','HISPANIC','WHITE','BLACK','NAMERICAN','ASIAN','age',
'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail','DEP1','ESTEEM1','VIOL1',
'PASSIST','DEVIANT1','SCHCONN1','GPA1','EXPEL1','FAMCONCT','PARACTV','PARPRES']
#predictors = data_clean[['BIO_SEX','HISPANIC','WHITE','BLACK','NAMERICAN','ASIAN','age',
#'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail','DEP1','ESTEEM1','VIOL1',
#'PASSIST','DEVIANT1','SCHCONN1','GPA1','EXPEL1','FAMCONCT','PARACTV','PARPRES']]            
#            
predictors = data_clean[all_features]
targets = data_clean.TREG1

#%%Split into training and testing sets
from sklearn.cross_validation import train_test_split
pred_train, pred_test, tar_train, tar_test  =   train_test_split(predictors, targets, test_size=.4)

pred_train.shape
pred_test.shape
tar_train.shape
tar_test.shape

#%% Build classifier using random forest 

from sklearn.ensemble import RandomForestClassifier

#Build model on training data
classifier=RandomForestClassifier(n_estimators=25) #number of tree
classifier=classifier.fit(pred_train,tar_train)

# apply randomforest model to get prediction for test data
predictions=classifier.predict(pred_test)

import sklearn.metrics
# Confusion Matrix
#              +---------------------------------------------+
#              |                Predicted label              |
#              +----------------------+----------------------+
#              |          (+1)        |         (-1)         |
#+-------+-----+----------------------+----------------------+
#| True  |(+1) | # of true positives  | # of false negatives |
#| label +-----+----------------------+----------------------+
#|       |(-1) | # of false positives | # of true negatives  |
#+-------+-----+----------------------+----------------------+
sklearn.metrics.confusion_matrix(tar_test,predictions)

# Accuracy
accuracy = sklearn.metrics.accuracy_score(tar_test, predictions)
print "Test Accuracy: %s" % accuracy

# fit an Extra Trees model to the data
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(pred_train,tar_train)
# display the relative importance of each attribute
#print(model.feature_importances_)

coeffients_data = pd.DataFrame(all_features, columns=['feature'])
coeffients_data['coefficients'] = model.feature_importances_
print coeffients_data

#%% Running a different number of trees and see the effect 
# of that on the accuracy of the prediction

trees=range(25)
accuracy=[]
for idx in range(len(trees)):
   classifier=RandomForestClassifier(n_estimators=idx + 1)
   classifier=classifier.fit(pred_train,tar_train)
   predictions=classifier.predict(pred_test)
   accuracy.append(sklearn.metrics.accuracy_score(tar_test, predictions))
   
import matplotlib.pyplot as plt   
#plt.cla()
plt.plot(trees, accuracy)
plt.grid(True)
plt.xlabel('Number of tree')
plt.ylabel('accuracy of model')
plt.title("Random Forest Classifier")
