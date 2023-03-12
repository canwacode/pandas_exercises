import pandas as pd 
import numpy as np
io = "C:\\Users\\zhongcan\\Desktop\\learnpy119\\pandas_exercises\\04_Apply\\US_Crime_Rates\\US_Crime_Rates_1960_2014.csv"

crime = pd.read_csv(io,sep=',')

### Step 4. What is the type of the columns? 两种方法：
crime.info()
all_col_dtype = crime.dtypes
some_col_dtype = all_col_dtype['Population']
# print(all_col_dtype) # df.dtypes是一个函数，它是pandas库中DataFrame对象的一个属性,返回每一列的数据类型.输出结果将会是一个Series对象，
# print(some_col_dtype)
#或者使用dtype函数：可以通过指定DataFrame中某一列的名称来获取该列的数据类型：比如：
crime['Population'].dtype
crime.Year = pd.to_datetime(crime.Year,format='%Y')
print(crime['Year'].dtype)

#将df的某一列设置为df的索引

crime = crime.set_index('Year',drop= True)   
crime = crime.drop('Total',axis=1)            # axis = 1 指删除整列，需要注意的是，drop函数不会修改原始DataFrame，而是返回一个新的DataFrame，所以需要将返回值重新赋值给df变量。
#或者使用del命令删除DataFrame中的某一列 ，会直接修改原始数据：
# del crime['Total']
# 如果想要删除多列，可以用del命令连续删除多列，或者使用drop函数一次性删除多列。
print(crime.head())

### Step 8. Group the year by decades and sum the values

#### Pay attention to the Population column number, summing this column is a mistake

# To learn more about .resample (https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.resample.html)
# To learn more about Offset Aliases (http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases)

# Uses resample to sum each decade
crimes = crime.resample('10AS').sum()

# Uses resample to get the max value only for the "Population" column
population = crime['Population'].resample('10AS').max()

# Updating the "Population" column
crimes['Population'] = population



### Step 9. What is the most dangerous decade to live in the US?
most_dangerous_decade = crimes.idxmax(0)#df.idxmax(0),它的作用是返回每列中最大值所在行的索引。这里的数字0表示在每列中查找最大值,会返回一个series，索引是列名，值是最大值所在行索引
crime.idxmax(1)#df.idxmax(1)，它的作用是返回每行中最大值所在列的标签。这里的数字1表示在每行中查找最大值，因为0是行标签，1是列标签
print(most_dangerous_decade)
