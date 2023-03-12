
# Step 1. Import the necessary libraries
import pandas as pd 
import numpy as np



url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url,sep = '\t')

print(chipo.head())


#请求价格超过10的商品
price_float = lambda x: float(x[1:-1])
item_price_float = chipo.item_price.apply(price_float)
chipo.item_price = item_price_float
niu=chipo[chipo['item_price']>10].head(10)
print('My name is {}'.format(niu))
#或者：
# clean the item_price column and transform it in a float
prices = [float(value[1 : -1]) for value in chipo.item_price]   
chipo.item_price = prices
#请求单价超过10的商品
# price_float1 = 0
# for value in chipo.item_price:
    # price_float1 = float(value[1:-1])
#chipo.item_price = price_float1

chipo_filtered = chipo.drop_duplicates(subset=['item_name','quantity'])
chipo_one_shohinn = chipo_filtered[chipo_filtered['quantity']==1]
chipo_one_priceover10 = chipo_one_shohinn[chipo_one_shohinn['item_price']>10]
priceover10_num = chipo_one_priceover10.item_name.count()     #.count（）只计数 不去重
priceover10_num2 = chipo_one_priceover10.item_name.nunique()  #.nunique()自带去重
print('My age is {}'.format(priceover10_num2))
#请求每个商品的单价
chipo_price_per_item = chipo_filtered[chipo_filtered['quantity']==1].loc[:,['item_name','quantity']]
#或者
chipo_price_per_item = chipo_filtered[chipo_filtered['quantity']==1][['item_name','quantity']]
print('My price is {}'.format(chipo_price_per_item))
#根据商品名字排序
chipo.sort_values(by='item_name')

chipo.sort_values("item_name",ascending = False)  # sort_value(默认ASC) 

#价格最贵的订单的商品数量是多少？
most_expensive_order = chipo.sort_values(by='item_price',ascending= False).head(1)
most_expensive_order.quantity 
print('My most_expensive_order is {}'.format(most_expensive_order.quantity))

#Veggie Salad Bowl被下单了多少次
chipo_Salad_Bowl = chipo[chipo['item_name']=='Veggie Salad Bowl']
order_times1 = chipo_Salad_Bowl['order_id'].count() 
order_times2 = chipo_Salad_Bowl.shape[0]
order_times3 = len(chipo_Salad_Bowl)         #python内置函数len()
print('how many times  {}'.format(order_times1))


# 一单超过1Canned Soda 的订单有多少单？
chipo_soda = chipo[chipo['item_name'] =='Canned Soda']
soda_twice = [chipo_soda['quantity'] > 1] #这种写法返回的是一个布尔型series
chipo_sodaover1_order_num = soda_twice.grouopby('order_id').sum('quantity').shape[0]
print(chipo_sodaover1_order_num)  

#或者两步二合一
chipo_soda_2in1 = chipo[chipo[chipo['item_name' =='Canned Soda']].quantity > 1] 
chipo_soda_2in1 = chipo[(chipo.item_name =='Canned Soda') & (chipo.quantity > 1)]  #多条件过滤的方法
len(chipo_soda_2in1)
chipo_soda_2in1.shape[0]




















