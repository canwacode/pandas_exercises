import pandas as pd 
import numpy as np

io = "C:\\Users\\zhongcan\\Desktop\\learnpy119\\pandas_exercises\\04_Apply\\Students_Alcohol_Consumption\\student-mat.csv"

df = pd.read_csv(io,sep=',')
##Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column

stud_alcoh = df.loc[:,'school':'guardian']
print(stud_alcoh.head())
create_lambda_func = lambda x: x.capitalize()    # python 函数 str.capitalize() 将字符串首字母大写化

## Step 6. Capitalize both Mjob and Fjob

stud_alcoh['Mjob'] = stud_alcoh['Mjob'].apply(create_lambda_func)
stud_alcoh['Fjob'] = stud_alcoh['Fjob'].apply(create_lambda_func)
# print(stud_alcoh.head())

## Step 7. Print the last elements of the data set.  打印最后一行的几种方法 复习.iloc[]函数
# stud_alcoh.info()
last_elements = stud_alcoh.iloc[394,:]
last_elements = stud_alcoh.iloc[-1,:]
last_elements = stud_alcoh.tail(1)
## Step 9. Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)
def majority(age):
    if age > 17:
        return True
    else:
        return False
stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(majority)   #在使用 apply() 方法时，需要传入一个函数名，而不是一个函数的调用结果。如果在 apply() 方法中加上括号 ()，就相当于对函数进行调用，而不是将函数名传给 apply() 方法。因此,这里majority不应该加括号。
# print(stud_alcoh.head())

def mut10(x):
    if type(x) is int:
        return x * 10
    return x                  #函数本身作用域里面尽量要有一个return来确保返回的安全性
stud_alcoh = stud_alcoh.applymap(mut10)

print(stud_alcoh.head())


# 本周重点：
# 对于某一列某一行的数据处理: df['col'].apply(func) 
# 对于将函数作用于整个dataset 所有元素：df.applymap(func)
