# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:45:11 2023

@author: antonov_dv
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_validate
from sklearn.metrics import accuracy_score

random_state = 123
data_model = pd.read_csv('data_model.csv')

# Поделим на выборки
data_features = data_model.drop('comp_fault', axis = 1)

data_target = data_model['comp_fault']
data_features_train, data_features_test, data_target_train, data_target_test = train_test_split(data_features, data_target,
                                                     test_size = 0.2, random_state = random_state)
print('Размеры выборок:')
print('Обучающие')
print(data_features_train.shape, data_target_train.shape)
print('Тестовые')
print(data_features_test.shape, data_target_test.shape)

param_grid={
    'n_estimators': np.arange(300, 500, 100),
    'max_features': ['sqrt', 'log2'],
    'max_depth' : np.arange(6, 8, 1)
    }

model = RandomForestClassifier(random_state, criterion='entropy')

GSCV = GridSearchCV(estimator=model, param_grid=param_grid, cv= 5, verbose = 10)

GSCV.fit(data_features_train, data_target_train)

print(GSCV.best_estimator_)

model = GSCV.best_estimator_
model.fit(data_features_train, data_target_train)

feature_importances = pd.DataFrame()
feature_importances['features'] = data_features_train.columns
feature_importances['importance'] = model.feature_importances_

print('Feature importances:')
print(feature_importances.sort_values(by = 'importance', ascending = False))

result = model.predict(data_features_test)
print('Accuracy:')
print(sklearn.metrics.accuracy_score(data_target_test, result))