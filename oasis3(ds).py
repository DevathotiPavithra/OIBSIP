# -*- coding: utf-8 -*-
"""oasis3(ds).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wiOfzKVzK0Ey1fI1czIUhc5SxfSDlH-c
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = {
    'Brand': ['Toyota', 'Honda', 'Nissan', 'Ford', 'Toyota'],
    'Features': [4, 2, 3, 2, 4],
    'Horsepower': [180, 200, 150, 170, 185],
    'Mileage': [30, 25, 28, 22, 29],
    'Price': [25000, 28000, 23000, 26000, 25500]
}
df = pd.DataFrame(data)
df

df = pd.get_dummies(df, columns=['Mileage'], drop_first=True)
X = df.drop('Price', axis=1)
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
df

model = LinearRegression()
model.fit(X_train, y_train)
model

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared (R2) Score: {r2}')