#多变量绘图分析
import numpy as npy
import pandas as pda
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style='whitegrid',color_codes=True)
npy.random.seed(sum(map(ord,'categorical')))
titanic = sns.load_dataset('titanic')
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')

#散点图分布
#sns.stripplot(x='day',y='total_bill',data=tips,jitter=True)#jitter:摆动,避免多点重叠
#plt.show()#横坐标左右小幅偏移都属于当天，纵坐标始终不变，表示当天的小费
'''
#点以树结构分布
sns.swarmplot(x='day',y='total_bill',hue='sex',data=tips) # hue='sex':图例参数
plt.show()

sns.swarmplot(x='total_bill',y='day',hue='time',data=tips)
plt.show()
'''
#盒图显示
sns.boxplot(x='day',y = 'total_bill',hue='time',data=tips)
plt.show()
#横向盒图
sns.boxplot(data=iris,orient='h')
plt.show()
'''
#小提琴显示 #split 参数表示小提琴两侧分开，显示图例的两种类别。
sns.violinplot(y='total_bill',x = 'day',hue='sex',data=tips,split=True)
plt.show()
#条形图显示 survived在这里显示的是平均获救率
sns.barplot(x='sex',y='survived',hue='class',data=titanic)
plt.show()
'''
'''
#点图更好的描述差异性
sns.pointplot(x='sex',y='survived',hue='class',data=titanic)
plt.show()
#添加参数在点图中,丰富样式
sns.pointplot(x='class',y='survived',hue='sex',data=titanic,\
              palette={'male':'g','female':'r'},\
              markers=['d','o'],linestyles=['-','--'])#
plt.show()
'''
sns.factorplot(x='day',y='total_bill',hue='smoker',data=tips,kind='bar')
plt.show() #palette:seaborn中的调色板
#添加参数实现多变量，各种类型作图   swarm：树结构
sns.factorplot(x='day',y='total_bill',hue='smoker',data=tips,kind='bar',col='time')
plt.show()
#col:按照此类型分类  size:图大小 aspect:纵横比  strip:散点
sns.factorplot(x='time',y='total_bill',hue='smoker',data=tips,kind='bar',col='day',size=5,aspect=.8)
plt.show()







































