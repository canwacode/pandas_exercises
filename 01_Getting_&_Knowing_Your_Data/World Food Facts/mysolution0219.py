import pandas as pd
import numpy as np


path = "C:\\Users\\zhongcan\\Desktop\\learnpy119\\pandas_exercises\\01_Getting_&_Knowing_Your_Data\\World Food Facts\\en.openfoodfacts.org.products.tsv\\en.openfoodfacts.org.products.tsv"

food = pd.read_csv(path, sep='\t')

first5entries = food.head()


#该数据集有多少条数据
num_of_observation = food.shape[0] 
#该数据集有多少列
num_of_columns = food.shape[1]
num_of_columns_rows = food.info()

col_name1 = food.columns
col_name2 = list(food)
col_name3 = food.keys()


#三种方式获取df的所有[列名]



col_name105 = food.columns[104]     #此处是易错点 ，第105列的列名，其实切片索引是104


col_name105_type1 = food.dtypes['-glucose_100g'] 
col_name105_type2 = food['-glucose_100g'].dtype

# print(col_name105_type2) 
how_indexed = food.index     # 可以看到行的起点索引和结束索引 ，以及步长 ：RangeIndex(start=0, stop=356027, step=1)

#几种获取某个单元格内容的方法 
cell_locate1 = food.loc [18,'product_name']
cell_locate2 = food.loc[18]['product_name']    # .loc函数只能用索引名或者列名 不能用数字
cell_locate2 = food.iloc[18]['product_name']   #.iloc函数只能用数字
cell_locate3 = food.values[18][7]
cell_locate4 = food.at[18,'product_name']
cell_locate5 = food.iat[18,7]
# print(cell_locate5)
food.columns.get_loc('code')     #.get_loc()是index数据类型里的函数，获取某个索引的列号

