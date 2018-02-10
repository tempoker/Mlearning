#单变量分析绘图
import numpy as npy
import pandas as pda
from scipy import stats,integrate
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl


x=npy.random.normal(size=100)#单变量->直方图 
sns.distplot(x,bins=20)#,kde=False:表示拟合线条,bins=18表示切分成18块
plt.show()

#根据均值和协方差生产数据     两个变量->散点图
mean,cov=[0,1],[(1,.5),(.5,1)]
data = npy.random.multivariate_normal(mean,cov,200)
df = pda.DataFrame(data,columns=['X','Y'])
sns.jointplot(x='X',y='Y',data=df)
plt.show()

mean,cov=[0,1],[(1,.5),(.5,1)]
x,y = npy.random.multivariate_normal(mean,cov,1000).T
with sns.axes_style('white'):#散点图：颜色深=密度大，六边形显示
     sns.jointplot(x=x,y=y,kind='hex',color='red')#数据大，用hex，color='k':black
plt.show()

#多变量，两两之间关系图
iris = sns.load_dataset('iris') #花瓣，花蕊长度宽度之间的关系
sns.pairplot(iris)#结果是4X4矩阵图，对角线上表示单变量，故采用直方图
plt.show()
#回归分析
sns.set(color_codes=True)
npy.random.seed(sum(map(ord,'regression')))
tips = sns.load_dataset('tips')
#print(tips.head()) #columns=(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
#sns.regplot(x='total_bill',y='tip',data=tips)
sns.regplot(x='size',y='tip',data=tips,x_jitter=.05)#x_jitter=.05:散点值小幅摆动
plt.show()


















