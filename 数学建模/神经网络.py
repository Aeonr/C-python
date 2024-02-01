from sklearn.neural_network import MLPClassifier
from numpy import array,r_,ones,zeros
for i in range(1,100):
    x0=array([[1.14 , 1.18, 1.20 , 1.26, 1.28, 1.30 , 1.24, 1.36 , 1.38 , 1.38,1.38 , 1.40 , 1.48, 1.54, 1.56] ,[1.78 , 1.96 , 1.86, 2.00 , 2.00 , 1.96, 1.72 , 1.74, 1.64, 1.82 ,1.90 , 1.70 , 1.82, 1.82 ,2.08]]).T
    y0=r_[ones(6),zeros(9)]
    md=MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=15)
print(md)
md.fit(x0,y0)
x=array([[1.24 , 1.80] , [1.28 , 1.84] , [1.40 ,2.04]])
pred=md.predict(x)
print(md.score(x0,y0))
print(md.coefs_)
print("属于各类的概率是:",md.predict_proba(x))
print("三个待判样本点类别是：",pred)
# from sklearn.neural_network import MLPClassifier
# from numpy import array,r_,ones,zeros
#
# b=0
# c=0
# for i in range(1,1000):
#     x0 = array([[1.14, 1.18, 1.20, 1.26, 1.28, 1.30, 1.24, 1.36, 1.38, 1.38, 1.38, 1.40, 1.48, 1.54, 1.56],
#                 [1.78, 1.96, 1.86, 2.00, 2.00, 1.96, 1.72, 1.74, 1.64, 1.82, 1.90, 1.70, 1.82, 1.82, 2.08]]).T
#     y0 = r_[ones(6), zeros(9)]
#     md = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=15)
#     md.fit(x0, y0)
#     x = array([[1.24, 1.80], [1.28, 1.84], [1.40, 2.04]])
#     a= md.predict(x)
#     if a[0]==1 and a[1]==0 and a[2]==1:
#         b+=1
#     else:
#         c+=1
# print(b,c)
