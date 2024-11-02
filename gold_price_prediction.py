# -*- coding: utf-8 -*-
"""Gold price-prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CwSQURxLlDrk4J-4CExz3dk98Zz871E_
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

gld_price= pd.read_csv('/gold_dataset.csv')

gld_price.head()

gld_price.tail()

gld_price.shape

gld_price.info()

gld_price.isnull().sum()

gld_price.describe()

gld_price['Date'] = pd.to_datetime(gld_price['Date'])
correlation = gld_price.drop(columns=['Date']).corr()

plt.figure(figsize = (8,8))
sns.heatmap(correlation,cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size': 8}, cmap= 'Blues')

print(correlation['GLD'])

sns.displot(gld_price['GLD'],color='Blue')

X = gld_price.drop(['Date','GLD'],axis=1)
Y = gld_price['GLD']

print(X)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2,random_state=2)

regressor = RandomForestRegressor(n_estimators=100)

regressor.fit(X_train,Y_train)
Y_pred = regressor.predict(X_test)

test_data_prediction = regressor.predict(X_test)

print(test_data_prediction)

error_score = metrics.r2_score(Y_test,test_data_prediction)
print("R squared error: ", error_score)

Y_test = list(Y_test)

plt.plot(Y_test, color = 'red', label = 'Actual Value')
plt.plot(test_data_prediction, color = 'blue', label = 'Predicted_Value')
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel ('GLD Price')
plt.legend()
plt.show()