# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:07:58 2019

@author: abdul
"""

'''this program is used to predict about te stars weather they will get a award or not
based on past data 
'''

#importing libraries that we needed
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

#reading the content from excel file
dataset = pd.read_excel('last_hope.xlsx')

#dealing with missing values/cells in dataset usign .fillna method
#all missing vakues are replaced with 'NA' keyword
dataset['star2'] = dataset['star2'].fillna(value='NA')
dataset['star3'] = dataset['star3'].fillna(value='NA')
dataset['star4'] = dataset['star4'].fillna(value='NA')

#making partitions of dataset into dependent and independent variables 
#third variable(x_pred) is the data that we need to predict
x = dataset.iloc[0:41, 9:13].values
y = dataset.iloc[0:41, 8].values
x_pred = dataset.iloc[224:231, 9:13].values
#for i in range(len(x)):
#    print(x[i], y[i])

#dealing with categorical data using labelencoder 
#all stars get replaced by specific integer values generated by LabelEncoder
encoder = LabelEncoder()
dataset['star1'] = encoder.fit_transform(dataset['star1'])
dataset['star2'] = encoder.fit_transform(dataset['star2'])
dataset['star3'] = encoder.fit_transform(dataset['star3'])
dataset['star4'] = encoder.fit_transform(dataset['star4'])

#building and training oue model
classifier = GaussianNB()
classifier.fit(x, y)

#making prediction of data/x_pred
pred = classifier.predict(x_pred)
