#import list
import pandas as pd
import numpy as np
#读取数据
data = pd.read_csv('house_train.csv',na_values=[" "])
print(data, '\n')
print(data.shape, '\n', type(data))
print(data.isnull().any(axis=0))
#缺失值的检测和缺失值处理
total=data.isnull().sum().sort_values(ascending=False)
percent=(data.isnull().sum() /
         data.isnull().count()).sort_values(ascending=False)
missing_data=pd.concat([total,percent],axis=1,keys=['缺失值的个数','所占百分比'])
print(missing_data)
#填充缺失值,用前一个非缺失值去填充该缺失值
data.fillna(method='ffill',inplace=True)
#异常值检测
#3sigma原则
def three_sigma_to_nan(data):
    for i in [0,1,3,4,7,8,9,10,11,12]: # 对每一列分别用3sigma原则处理
        Ser1 = data.iloc[:,i]
        rule = (Ser1.mean()-3*Ser1.std()>Ser1) | (Ser1.mean()+3*Ser1.std()< Ser1)
        rule = np.array(rule)
        data.iloc[rule,i] = np.nan
    return data
cleaned_data=three_sigma_to_nan(data)
cleaned_data.fillna(method='ffill',inplace=True)
data.to_csv('cleaned_data.csv', index=False)














