import pandas as pd
path = "C:\\Users\\zhongcan\\Desktop\\learnpy119\\pandas_exercises\\03_Grouping\\Occupation\\u.users.txt"
users = pd.read_table(path,sep="|",index_col='user_id')

mean_age_peroccu  = users.groupby('occupation').age.mean()
doc_malecount = users[(users['occupation'] == 'engineer') & (users['gender']=='M')][['occupation','gender']].value_counts()
users.groupby('occupation').age.agg(['max','min'])
groupby_combination = users.groupby(['occupation','gender']).mean()



#本章重难点：在 Pandas 中，两个 Series 相除的运算规则是：按照索引对应的关系进行相除，如果两个 Series 中存在不同的索引，则会使用 NaN 进行填充。
#create一个能将M、F字符串转换为数值的函数

def gender_to_count(gender):
    if gender =='M': 
     return 1
    if gender =='F':
     return 0
users['gender_count'] = users['gender'].apply(gender_to_count)
# users['gender_count'] = [users['gender'].apply(gender_to_count) for value in users.gender]#这行代码中的 apply() 方法可以直接作用于 Series 对象，不需要使用列表推导式
# male_ratio_divdirectly = users.groupby('occupation').gender_count.sum() / users.occupation.value_counts().mul(100) 
# male_ratio_divdirectly.sort_values(ascending = False)
# 先分别定义分子分母 再用.div()除
df1 = users.occupation.value_counts()   # 返回的是series
df2 = users.groupby('occupation',sort=False).gender_count.sum() # 返回的是series
print('df1{}'.format(df1))
print('df2{}'.format(df2))
male_ratio_two_series_div =round(df2.div(df1).mul(100),2)   # / 替换为 Pandas 提供的除法运算符 div()  # round()函数用法和excel，sql一样
male_ratio_two_series_div.sort_values(ascending=False)
print(male_ratio_two_series_div)



    