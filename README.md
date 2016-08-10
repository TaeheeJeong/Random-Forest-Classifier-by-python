## Random Forest Classifier by python

Random forest analysis was performed to evaluate the importance of a series of explanatory variables in predicting a binary, categorical response variable.   
The following explanatory variables were included as possible contributors to a random forest evaluating.   
(categorical)    
'BIO_SEX','HISPANIC','WHITE','BLACK','NAMERICAN','ASIAN','ALCEVR1','marever1','cocever1','inhever1','cigavail','PASSIST','EXPEL1',   
(quantitative)    
'age','ALCPROBS1','DEVIANT1','VIOL1','DEP1','ESTEEM1','PARPRES','PARACTV','FAMCONCT','SCHCONN1','GPA1'   

The explanatory variables with the highest relative importance scores were 'marever1', 'GPA1', 'DEVIANT1'.
The explanatory variables with the lowest relative importance scores were 'ASIAN' and 'NAMERICAN'.
The accuracy of the random forest was 83%, with the subsequent growing of multiple trees rather than a single tree, adding little to the overall accuracy of the model, and suggesting that interpretation of a single decision tree may be appropriate.

This is Classifier by Random Forest method using python.  
data set: tree_addhealth.csv
Classifier: Random forest from sklearn

# Confusion Matrix
array([[1408,   80],       
..........[ 227,  115]])
         
+-------+-----+----------------------+-------------+   
|  # of true positives  |   # of false negatives |   
| +-----+----------------------+------------------+   
|  # of false positives |   # of true negatives  |   
+-------+-----+----------------------+-------------+   


Test Accuracy: 0.832240437158

# relative importance of each attribute  
      feature  coefficients  
7    marever1      0.100845   
23       GPA1      0.080363   
15   DEVIANT1      0.066805   
17       DEP1      0.066544   
21   FAMCONCT      0.063626   
22   SCHCONN1      0.062392   
13        age      0.058862   
20    PARACTV      0.056902   
18    ESTEEM1      0.052570   
6     ALCEVR1      0.050948   
16      VIOL1      0.049458   
14  ALCPROBS1      0.047906   
19    PARPRES      0.047304  
2       WHITE      0.028462   
10   cigavail      0.028048   
0     BIO_SEX      0.026409   
8    cocever1      0.020719   
11    PASSIST      0.018014   
3       BLACK      0.017155   
1    HISPANIC      0.015145   
9    inhever1      0.013350   
12     EXPEL1      0.012288   
4   NAMERICAN      0.008662  
5       ASIAN      0.007223   

