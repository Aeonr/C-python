import numpy as np
import pandas as pd


def SNHT_change_point_detection(inputdata):
    inputdata = np.array(inputdata)
    inputdata_mean = np.mean(inputdata)
    n = inputdata.shape[0]
    k = range(1,n)
    sigma = np.sqrt(np.sum((inputdata-np.mean(inputdata))**2)/(n-1))
    Tk = [x*(np.sum((inputdata[0:x]-inputdata_mean)/sigma)/x)**2 + (n-x)*(np.sum((inputdata[x:n]-inputdata_mean)/sigma)/(n-x))**2 for x in k]
    T = np.max(Tk)
    K = list(Tk).index(T) + 1
    return year[K-1]

d = pd.read_excel('E:\\建模比赛\\咸阳日径流1979-2019.xlsx', sheet_name='Sheet3')
inputdata = d['咸阳年径流']
year=d['年']

print(SNHT_change_point_detection(inputdata))