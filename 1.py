import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv('https://raw.githubusercontent.com/okfn/dataportals.org/master/data/portals.csv')
print(df)
df.isnull()
size=df.size
shape=df.shape
df_ndim=df.ndim
series_ndim=df["name"].ndim
print("Size = {}\nShape = {}\nShape[0] * Shape[1] = {}\nDataFrame ndim = {}\nSeries ndim = {}".format(
    size, shape, shape[0] * shape[1], df_ndim, series_ndim))
dataTypeSeries=df.dtypes
print("data type of each of each column of dataframe is :")
print(dataTypeSeries)
dummies = pd.get_dummies(df.author)
merged = pd.concat([df, dummies], axis='columns')
merged.drop(['author'],axis='columns')
print(merged)








