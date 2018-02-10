#heatmap 热度图
import numpy as npy
import matplotlib.pyplot as plt
npy.random.seed(0)
import seaborn as sns

sns.set()
data = npy.random.randn(3,3)#矩阵的值的索引与热度图位置对应。
print(data) #,vmax=0.9,vmin=0.2
heatmap = sns.heatmap(data,center=0)#vmax,vmin表示重置右边调色板的取值范围
plt.show()
fts = sns.load_dataset('flights')
fgh=fts.pivot('month','year','passengers')
print(fgh.head())
ax = sns.heatmap(fgh,annot=True,fmt='d',linewidth=.5) #在渐变图中加入数据 annot=True：显示注释 fmt:显示的字体 linewidth=.5表示格子间距
plt.show() #,cmap='YlGnBu':调色板
