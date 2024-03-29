import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import statsmodels.formula.api as smf
import csv

path= 'C:\\Users\\CYH10\\Desktop\\DID.csv'
f = pd.read_csv(path)
data = f[['pid', 'year', 'Phealth', 'time', 'treat']]  # 读取指定行
reader = list(csv.reader(data))
print(reader)
for row in reader:
    print(row)
# data.Phealth = np.array(data.Phealth, dtype=np.float)
# data.Phealth = np.array(data.Phealth, dtype=np.float)
# before_treat = data[data['time'] == 0]
# data.info()
# model = smf.ols('Phealth ~ treat*year', data=before_treat).fit()
data.info()
# print(model.summary())