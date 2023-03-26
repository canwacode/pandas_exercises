import pandas as  pd
import numpy as np

path1 = "C:\\learnpython\\pandas_exercises\\05_Merge\\Auto_MPG\\cars1.csv"
path2 = "C:\\learnpython\\pandas_exercises\\05_Merge\\Auto_MPG\\cars2.csv" 

car1 = pd.read_csv(path1,sep=',')
car2 = pd.read_csv(path2,sep=',')

#删除cars1中为缺失值的列 ：
car1 = car1.dropna(axis=1)    #dropna(axis = 1 表示删除列，inplace = True 代表直接修改原始数据)
car1 = car1.loc[:,'mpg':'car']

# print(f'car1表 一共有几行：{car1.shape[0]}')
# print(f'car2表 一共有几行：{car2.shape[0]}')

# join car1 and car2 into one dataset 
cars = pd.concat([car1,car2],axis=0,ignore_index= True)
# print(f'rows merge into one cars :\n{cars.tail()}')


col_owners = pd.Series(np.random.randint(15000,73000,size=398))    #low = 15000,high = 73000 前闭后开
cars['col_owners'] = col_owners
# print(cars.tail())
# 使用了 numpy 库中的 np.random.randint() 函数生成了一个长度为 10 的随机整数数组，然后将该数组转换为series对象

print(cars.dtypes)








