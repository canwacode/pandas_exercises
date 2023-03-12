import pandas as pd


raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}
# army = army.set_index('origin')

#组合起来，创建一个以origin为index的df的方法：注意比较两种方式的不同，第一种保留index的名字origin，第二种不会保留，不会有多出一行空白行origin

#方法一
# origin = ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']
# army  = pd.DataFrame(raw_data,index=origin)
# del army['origin']   #或者 用drop('列名'，axis = 1 ,inplace=True)来删除某一列 army = army.drop('origin',axis=1,inplace=True)   
# print('armyone{}'.format(army.head(2)))

#方法二
army = pd.DataFrame(data=raw_data)
army = army.set_index('origin')
# print('army{}'.format(army.head(2)))

armyve_and_deaths = army.loc[:,['deaths','veterans']]
print(armyve_and_deaths)

army_veterans = army['veterans']
army_veterans = army.veterans
army_veterans = army.loc[:,['veterans']] 
army_veterans_deaths = army.loc[:,['veterans','deaths']]

army.columns   # 返回一个 按列名顺序排列的列名的列表
army.info() 

army_Maine_Alask = army.loc[:,['veterans','deaths']].loc[['Maine','Alaska']]
#或者 
army_Maine_Alask = army.loc[['Maine','Alaska'],['veterans','deaths']]


army_3to7_3to6 = army.iloc[2:7,2:6]

#返回所有第四行之后的行和列
army.iloc[4:]

army.iloc[:4]
#   或者: |  和: & 非: ~  不等于 !=
army[(army.deaths > 500) | ( army.deaths < 50)]  
army[(army['deaths'] > 500) | (army['deaths'] < 50)]
army[army['regiment'] !='Dragoons']   # 不等于!= 可以用于排除数值 或者字符串
#返回索引为texas 和Arizona的所有行和列
army.loc[['Texas','Arizona'],:]
#返回某个单元格
army.loc['Arizona','deaths']
army_singlecell_at =army.at['Arizona','deaths']
army.loc['Texas','deaths']   # .loc只能用index和columns来取 .iloc 只能用数字索引
army.iloc[2,army.columns.get_loc('deaths')]     #df.columns.get_loc('deaths')是index数据类型里的函数，获取某个索引的列号

####本章重点:
#df.loc['one':'three','three':'five']  与df.loc[['one','three'],['three','five']] 思考区别是什么
#df.iloc[[3,0],[1,2]] 与 df.iloc[[0:3],[2:4]] 思考区别是什么

print(army.columns)
