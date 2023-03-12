import pandas as pd
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
regiment = pd.DataFrame(data= raw_data)
regiment.head(20)


Nighthawks_mean = regiment[regiment["regiment"] == "Nighthawks"].mean()
print(Nighthawks_mean)   #df.mean()  不是df.means() !!!!! 切记 勿忘  

#用于多级索引
# unstack() 方法可以将一个多级索引的 DataFrame 转换成一个新的 DataFrame，其中的一级行索引变为新 DataFrame 的行索引，而一级列索引变为新 DataFrame 的列索引。一般情况下，unstack() 方法需要指定要转换的行或列索引的级别（level），如果不指定，则默认转换最内层的索引。
# stack() 方法可以将一个 DataFrame 中的列索引转换成行索引，生成一个 Series。与 unstack() 方法类似，stack() 方法也需要指定要转换的行或列索引的级别，如果不指定，则默认转换最内层的索引
import pandas as pd
# 创建一个 DataFrame
data = {
    'nmamaa': ['John', 'Mike', 'Sarah', 'Jessie', 'Tom'],
    'regiment': ['red', 'blue', 'blue', 'green', 'red'],
    'age': [25, 35, 28, 29, 33],
    'gender': ['male', 'male', 'female', 'female', 'male']
}
df = pd.DataFrame(data)
# 按照 regiment 列进行分组
groups = df.groupby('regiment')
# 遍历每个分组，输出名称和数据
for name, group in groups:
    # print('Regiment:', name)
     print(group)
