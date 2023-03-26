import pandas as pd
import numpy as np
### Step 2. Create 3 differents Series, each of length 100, as follows: 
# 1. The first a random number from 1 to 4 
# 2. The second a random number from 1 to 3
# 3. The third a random number from 10,000 to 30,000

S1 = pd.Series(np.random.randint(1,5,size=100,dtype='l'))
S2 = pd.Series(np.random.randint(1,4,size=100,dtype='l'))
S3 = pd.Series(np.random.randint(10000,30000,size=100,dtype='l'))

# print(S1.head(5))
# print(S2.head(5))
# print(S3.head(5))

housemkt = pd.concat([S1,S2,S3], axis=1)     # 表的join
print(housemkt.head(5))
#修改列名的方式-直接列表赋值
housemkt.columns = ['bedrs','bathrs','price_sqr_meter']
print(housemkt.head(5))

bigcolumn = pd.concat([S1,S2,S3], axis=0)
print(bigcolumn.head(5))

# 将一个series转成一个dataframe的两种方式
df_bigcolumn = bigcolumn.to_frame() 
df_bigcolumn = pd.DataFrame(bigcolumn)

df_bigcolumn.reset_index(drop=True ,inplace= True)
#修改索引的方式
df_bigcolumn.index = pd.RangeIndex(1,301)

#修改列名的方式 df.rename()函数，括号里面写 旧名：新名
df_bigcolumn.rename (columns = {0:'col01'},inplace=True)
print(df_bigcolumn.tail(5))





