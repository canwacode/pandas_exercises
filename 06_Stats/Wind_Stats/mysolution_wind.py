import pandas as  pd
import numpy as np
import datetime #datetime 是Python标准库中的一个模块，主要用于处理日期和时间。
path_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'

windstats = pd.read_csv(path_url,sep="\s+",parse_dates =[[0,1,2]])

# print(windstats.head(5))

def fix_century(x):
  year = x.year - 100 if x.year > 1989 else x.year
  return datetime.date(year, x.month, x.day)         #datetime.date(year, x.month, x.day) 是 Python 中 datetime 模块中的一个函数，用于创建一个日期对象。这个函数接受三个参数，分别是年份、月份和日期。其中，年份是一个整数，表示日期的年份；月份也是一个整数，表示日期的月份，取值范围为 1-12；日期也是一个整数，表示日期的天数，取值范围为 1-31

# apply the function fix_century on the column and replace the values to the right ones
windstats['Yr_Mo_Dy'] = windstats['Yr_Mo_Dy'].apply(fix_century)

windstats['Yr_Mo_Dy'] = pd.to_datetime(windstats['Yr_Mo_Dy'])
windstats.rename (columns= {'Yr_Mo_Dy':'yearmonthday'},inplace = True)
windstats = windstats.set_index ('yearmonthday')
print(windstats.head(5))

# print(windstats['yearmonthday'].dt.day.dtypes)  #可以使用 pandas.Series.dt 属性来访问包含在日期时间中的日期部分（例如年、月、日等）
# print(windstats['yearmonthday'].dtypes)
print(windstats.index.to_series().dt.day.dtypes)  # 当yearmonthday变成df的index后，windstats['yearmonthday']这种写法就会报错，获取不到这一列，要用windstats。index.day来提取datetimeindex的日期部分

# 快速获取df里，每一列里有多少个缺失值 和非缺失值 数量：

windstats.isnull().sum()     #isnull() 方法判断 DataFrame data 中的每个元素是否缺失，返回一个布尔类型的 DataFrame,在python里，true为1，false为0，所以布尔型df也可以用.sum()
windstats.notnull().sum()
non_counts = windstats.shape[0] - windstats.isnull().sum()  #  '-'运算符的计算规则。当一个整数减去一个 Series 时，Pandas 会将整数广播到 Series 的每个元素上，然后进行逐元素的减法运算。
print(non_counts)

day_stats = pd.DataFrame(index=windstats.index)
day_stats['min'] = windstats.min(axis=1)
day_stats['max'] = windstats.max(axis=1)
day_stats['mean'] = windstats.mean(axis=1)
day_stats['std'] = windstats.std(axis=1)

print(day_stats.head())

windstats_Jau =  windstats.loc[windstats.index.to_series().dt.month ==1].mean()
print(windstats_Jau)
annualy_mean = windstats.resample('A').mean()
print(annualy_mean)
monthly_mean = windstats.resample('M').mean()
print(monthly_mean)
weekly_agg1 = pd.DataFrame(windstats.resample('W').agg(['mean','min','max','std'])).iloc[1:53,0:2].head()   
#或者用.loc() 得到前52周的index：
weekly = windstats.resample('W').agg(['mean','min','max','std'])
weekly_agg2 = weekly.loc[weekly.index[1:53],'RPT':'MAL'].head()
print(weekly_agg1) 
print(f'与weekly_agg1是一样的\n{weekly_agg1}') 
