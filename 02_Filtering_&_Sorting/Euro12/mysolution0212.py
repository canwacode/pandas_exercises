import pandas as pd 
import numpy as np

path = "C:\\Users\\zhongcan\\Desktop\\learnpy119\\pandas_exercises\\02_Filtering_&_Sorting\\Euro12\\Euro_2012_stats_TEAM.csv"

euro12 =pd.read_csv(path, sep=',')

#print(euro12.head(10))

goals = euro12.Goals 
# print(goals)     
# ? why head all df column stay,but head local no columns


# 去重函数 df['name'].drop_duplicates()
# 至少三种方式表达一共有多少支队伍，求指定列的去重计数
team_num = euro12.shape[0]
team_num = euro12['Team'].value_counts().count()
team_num = len(euro12.Team.drop_duplicates())

#返回一共有多少列的几种方法
col_num = euro12.shape[1] 
euro12.info()
euro12.shape 

discipline = euro12[['Team','Yellow Cards','Red Cards']]  #注意 df只选一列一对[],选取多列 [[]]

euro12.columns.get_loc('Team')   #补充 ： 用 。get_loc() 函数： df.columns.get_loc('列名')  返回列所在的index位置

discipline = discipline.sort_values(by=['Red Cards', 'Yellow Cards'],ascending=False, na_position= 'first', inplace= False)
discipline = discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)

# print(discipline)

Yellow_means = euro12['Yellow Cards'].mean()

# print(round(Yellow_means,2))

goals6 = euro12.Goals > 6       #思考两者的不同？  上面返回的是一个bool 的series 下面是筛选之后的所有行
goals6 = euro12[euro12['Goals']> 6] 
#print(goals6)

teamstartwithG = euro12[euro12['Team'].str.startswith('G')]
#print(teamstartwithG) 

selectfirstsevencolumns = euro12[:][0:7]
# print(selectfirstsevencolumns) 

selectallexceptlastthree = euro12[:][0:-3]
#print(selectallexceptlastthree) 



# 以下两种写法均可，.iloc[] 不是函数
ShootingAccuracy1 = euro12[euro12['Team'].isin(['England','Italy','Russia'])][['Team','Shooting Accuracy']]
ShootingAccuracy1 = euro12[euro12['Team'].isin(['England','Italy','Russia'])].iloc[:,[0,4]]              #.iloc[] 只能填数字，[:,[3,4,5]] 来表示选取第3，4，5列
ShootingAccuracy1 = euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]
#print(ShootingAccuracy1)


#有多少种进球数？
goals_num = euro12.Goals

print(goals_num)

