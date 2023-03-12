import pandas as pd
path = "C:\\Users\\zhongcan\\Desktop\\learnpy119\\pandas_exercises\\03_Grouping\\Alcohol_Consumption\\drinks.csv"
drinks = pd.read_csv(path)
# print(drinks)

beer_mean_top1 = drinks.groupby('continent').beer_servings.mean().sort_values(ascending=False).head(1)
wine_describe = drinks.groupby('continent').wine_servings.describe()
mean_alcohol = drinks.groupby('continent').mean()
median_alcohol = drinks.groupby('continent').median()
spirit_agg = drinks.groupby('continent').spirit_servings.agg(['mean','min','max'])

print('beer_mean_top1{}'.format(beer_mean_top1))
print('wine_describe{}'.format(wine_describe))
print('mean_alcohol{}'.format(mean_alcohol))
print('median_alcohol{}'.format(median_alcohol))
print('spirit_agg{}'.format(spirit_agg))









