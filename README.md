## Random Forest Classifier by python

Random forest analysis was performed to evaluate the importance of a series of explanatory variables in predicting a binary, categorical response variable.   
The following explanatory variables were included as possible contributors to a random forest evaluating.   
(categorical)    
'BIO_SEX','HISPANIC','WHITE','BLACK','NAMERICAN','ASIAN','ALCEVR1','marever1','cocever1','inhever1','cigavail','PASSIST','EXPEL1',   
(quantitative)    
'age','ALCPROBS1','DEVIANT1','VIOL1','DEP1','ESTEEM1','PARPRES','PARACTV','FAMCONCT','SCHCONN1','GPA1'   

The explanatory variables with the highest relative importance scores were 'marever1', 'age', 'ESTEEM1'.   
The accuracy of the random forest was 83%, with the subsequent growing of multiple trees rather than a single tree, adding little to the overall accuracy of the model, and suggesting that interpretation of a single decision tree may be appropriate.

This is Classifier by Random Forest method using python.  
data set: tree_addhealth.csv
Classifier: Random forest from sklearn

# Confusion Matrix
array([[1408,   80],
          [ 227,  115]])
+-------+-----+----------------------+-------------+   
|  # of true positives  |   # of false negatives |   
| +-----+----------------------+------------------+   
|  # of false positives |   # of true negatives  |   
+-------+-----+----------------------+-------------+   


Test Accuracy: 0.832240437158

# relative importance of each attribute  
      feature  coefficients  
0       BIO_SEX        0.026043  
1      HISPANIC        0.014489  
2         WHITE        0.024664  
3         BLACK        0.022746  
4     NAMERICAN        0.007776  
5         ASIAN        0.004993  
6           age        0.061536   
7       ALCEVR1        0.052870    
8     ALCPROBS1        0.054727  
9      marever1        0.107234  
10     cocever1        0.013068  
11     inhever1        0.022722  
12     cigavail        0.026321  
13         DEP1        0.053687  
14      ESTEEM1        0.055718  
15        VIOL1        0.049204  
16      PASSIST        0.014063  
17     DEVIANT1        0.063653  
18     SCHCONN1        0.065462  
19         GPA1        0.074270  
20       EXPEL1        0.012950  
21     FAMCONCT        0.060176  
22      PARACTV        0.059759  
23      PARPRES        0.051868  

