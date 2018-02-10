#Facetgrid 用法主要用于子图
import numpy as npy
import pandas as pda
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid',color_codes=True)
npy.random.seed(sum(map(ord,'categorical')))

tips = sns.load_dataset('tips') #col:子图分类依据  hue:图中数据分类显示
iris = sns.load_dataset('iris')
g = sns.FacetGrid(tips,col='sex',hue='smoker')#alpha:透明程度，越大越深
g.map(plt.scatter,'total_bill','tip',alpha=.7) #scatter:散点图，近似马赛克
g.add_legend(loc='best')#图例显示hue的解释
plt.show()

g = sns.FacetGrid(tips,row='smoker',col='time',margin_titles=True)#margin_titles=True:边缘显示标题
g.map(sns.regplot,'size','total_bill',fit_reg=True,x_jitter=.1)
g.add_legend(loc='best')
plt.show()
'''
g = sns.FacetGrid(tips,col='day',size=5,aspect=.5)
g.map(sns.barplot,'sex','total_bill')
#g.add_legend(loc='best')
plt.show()

from pandas import Categorical
#order=tips.day.value_counts().index
order = Categorical(['Thur','Fri','Sat','Sun']) #子图按顺序显示order
g = sns.FacetGrid(tips,row='day',row_order=order,size=1.8,aspect=2.4)
g.map(sns.barplot,'total_bill')
plt.show()
'''
'''
pal = dict(Lunch='seagreen',Dinner='gray')
g = sns.FacetGrid(tips,hue='time',palette=pal,size=5) #调色板palette可以调用模板'Set2'
g.map(plt.scatter,'total_bill','tip',s=50,alpha=.7,linewidth=.5,edgecolor='white')
g.add_legend()
plt.show()
'''
with sns.axes_style('white'):
     g= sns.FacetGrid(tips,row='sex',col='smoker',margin_titles=True,size=2.5)
g.map(plt.scatter,'total_bill','tip',color='#334488',lw=.5)
g.set(xticks=[10,30,50],yticks=[2,6,10])
g.fig.subplots_adjust(wspace=.02,hspace=.02)#子图之间的宽和高距离
plt.show()
'''
g = sns.PairGrid(iris,hue='species')#花瓣分类
g.map_diag(plt.hist)#对角线的设置
g.map_offdiag(plt.scatter)
g.add_legend()
plt.show()

#变量多，取其中两个
g = sns.PairGrid(iris,vars=['sepal_length','sepal_width'],hue='species')
g.map(plt.scatter)
plt.show()
'''
g = sns.PairGrid(tips,hue='size',palette='Set3')#GnBu_d:渐变色
g.map(plt.scatter,s=50)
g.add_legend()
plt.show()







