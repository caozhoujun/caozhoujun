#import list
import pandas as pd
import numpy as np
import sklearn.preprocessing as skp
#读取数据
data = pd.read_csv('cleaned_data.csv')
#标准化
print(data.describe())
price_df=data[['price']]
price_array=np.array(price_df)
print(price_array)
price_st=skp.scale(price_array)
print(price_st,'\n')
#离散化
#先把高维数组转化成一维数组，以满足pd.cut（）的需要
price_array_new=list(np.array(price_array).flatten())
k=5
d1 = pd.cut(price_array_new, k, labels=range(k))
#找出与price相关性最高的三个特征并给出合理的解释
price=data.price
distirct=data.distirct
green_rate=data.green_rate
area=data.area
traffic=data.traffic
shockproof=data.shockproof
school=data.school
crime_rate=data.crime_rate
pm25=data.pm25
#自定义一个相关系数的函数
def corr_price(array1,array2):
    ab=np.array([array1,array2])
    dfab=pd.DataFrame(ab.T,columns=['array1','array2'])
    corr=dfab.array1.corr(dfab.array2)
    return corr
#输出相关系数
for i in [distirct,green_rate,area,traffic,shockproof,school,crime_rate,pm25]:
    print("与价格的相关系数为：",corr_price(price,i))

