# %load q01_myXGBoost/build.py
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from unittest import TestCase
from inspect import getargspec

# load data
dataset = pd.read_csv('data/loan_clean_data.csv')
# split data into X and y
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=9)

param_grid1 = {'max_depth': [2, 3, 4, 5, 6, 7, 9, 11],
               'min_child_weight': [4, 6, 7, 8],
               'subsample': [0.6, .7, .8, .9, 1],
               'colsample_bytree': [0.6, .7, .8, .9, 1]
               }


# Write your solution here :
def myXGBoost(X_train, X_test, y_train, y_test, model, param_grid, Kfold=3, **kwargs):
    gs_cv = GridSearchCV(estimator = model, param_grid= param_grid, cv = Kfold)
    gs_cv.fit(X_train, y_train)
    
    # make predictions for test data
    y_pred = gs_cv.predict(X_test)
    predictions = [round(value) for value in y_pred]

    accuracy = accuracy_score(y_test, predictions)
    #print('Accuracy: %.2f%%' % (accuracy * 100.0))
    
    return accuracy, gs_cv.best_params_

xgb = XGBClassifier(seed=9)
gs_cv_accuracy, gs_cv_best_params = myXGBoost(X_train, X_test, y_train, y_test, xgb, param_grid1, 3)
expected_best_params = {'subsample': 0.8, 'colsample_bytree': 0.7, 'max_depth': 2, 'min_child_weight': 4}
expected_accuracy = 0.796703296703

print (gs_cv_accuracy)
print (gs_cv_best_params)

args = getargspec(myXGBoost)
print (len(args[0]))
print (args[3])
print (type(gs_cv_accuracy))
print (type(gs_cv_best_params))

