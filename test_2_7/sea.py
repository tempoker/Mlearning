#2018-02-10 01:18:76 开始学习Seaborn
import seaborn as sns
import numpy as npy
import matplotlib as mpl
import matplotlib.pyplot as plt

def sinplot(flip=1):
     x = npy.linspace(0,14,100)
     for i in range(1,7):
          plt.plot(x,npy.sin(x+i*.5)*(7-i)*flip)
sns.set()#引进seaborn默认的参数设置
sinplot()
#sns.despine()
plt.show()

sns.set_style('ticks')#seaborn默认五种风格,whitegrid,white,dark,ticks,darkgird
data = npy.random.normal(size=(20,6))+npy.arange(6)/2
sns.boxplot(data)
sns.despine()#去掉上边+右边的边线
plt.show() 
#2018-02-10 01:44:98 睡觉，明天学完seaborn画图风格，开始入门算法。
