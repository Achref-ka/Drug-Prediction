# Decision Trees

import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import sklearn.tree as tree




'''
About the dataset
Imagine that you are a medical researcher compiling data for a study. 
You have collected data about a set of patients, all of whom suffered from the same illness. 
During their course of treatment, each patient responded to one of 5 medications, Drug A, Drug B, Drug c, Drug x and y.

Part of your job is to build a model to find out which drug might be appropriate for a future patient with the same illness. 
The features of this dataset are Age, Sex, Blood Pressure, and the Cholesterol of the patients, and the target is the drug that each patient responded to.

It is a sample of multiclass classifier, and you can use the training part of the dataset to build a decision tree, 
and then use it to predict the class of an unknown patient, or to prescribe a drug to a new patient.
'''

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv'


my_data = pd.read_csv(url, delimiter=",")
my_data[0:5]


print(my_data.shape)


# Pre-processing
# Using my_data as the Drug.csv data read by pandas, declare the following variables:

# X as the Feature Matrix (data of my_data)
# y as the response vector (target)
# Remove the column containing the target name since it doesn't contain numeric values.


X = my_data[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
X[0:5]

# As you may figure out, some features in this dataset are categorical, such as Sex or BP. Unfortunately, Sklearn Decision Trees does not handle categorical variables. 
# We can still convert these features to numerical values using LabelEncoder to convert the categorical variable into numerical variables.

from sklearn import preprocessing

le_sex = preprocessing.LabelEncoder()
le_sex.fit(['F','M'])
X[:,1] = le_sex.transform(X[:,1]) 


le_BP = preprocessing.LabelEncoder()
le_BP.fit([ 'LOW', 'NORMAL', 'HIGH'])
X[:,2] = le_BP.transform(X[:,2])


le_Chol = preprocessing.LabelEncoder()
le_Chol.fit([ 'NORMAL', 'HIGH'])
X[:,3] = le_Chol.transform(X[:,3]) 

X[0:5]

# Now we can fill the target variable.

y = my_data["Drug"]
y[0:5]

# Setting up the Decision Tree
# We will be using train/test split on our decision tree. Let's import train_test_split from sklearn.cross_validation.

from sklearn.model_selection import train_test_split

# Now train_test_split will return 4 different parameters. We will name them:
# X_trainset, X_testset, y_trainset, y_testset

# The train_test_split will need the parameters:
# X, y, test_size=0.3, and random_state=3.

# The X and y are the arrays required before the split, the test_size represents the ratio of the testing dataset, and the random_state ensures that we obtain the same splits.

X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)

# Practice
# Print the shape of X_trainset and y_trainset. Ensure that the dimensions match.


print('Shape of X training set {}'.format(X_trainset.shape),'&',' Size of Y training set {}'.format(y_trainset.shape))


# Print the shape of X_testset and y_testset. Ensure that the dimensions match.

print('Shape of X training set {}'.format(X_testset.shape),'&',' Size of Y training set {}'.format(y_testset.shape))

# Modeling
# We will first create an instance of the DecisionTreeClassifier called drugTree.
# Inside of the classifier, specify criterion="entropy" so we can see the information gain of each node.

drugTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
drugTree # it shows the default parameters

# Next, we will fit the data with the training feature matrix X_trainset and training response vector y_trainset

drugTree.fit(X_trainset,y_trainset)

# Prediction
# Let's make some predictions on the testing dataset and store it into a variable called predTree.

predTree = drugTree.predict(X_testset)

# You can print out predTree and y_testset if you want to visually compare the predictions to the actual values.

print (predTree [0:5])
print (y_testset [0:5])

# Evaluation
# Next, let's import metrics from sklearn and check the accuracy of our model.

from sklearn import metrics
import matplotlib.pyplot as plt

print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_testset, predTree))

# Accuracy classification score computes subset accuracy: the set of labels predicted for a sample must exactly match the corresponding set of labels in y_true.

# In multilabel classification, the function returns the subset accuracy. If the entire set of predicted labels for a sample strictly matches with the true set of labels, then the subset accuracy is 1.0; otherwise it is 0.0.

# Visualization
# Let's visualize the tree



tree.plot_tree(drugTree)
plt.show()
