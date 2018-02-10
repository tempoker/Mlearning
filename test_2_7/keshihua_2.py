import matplotlib.pyplot as plt
import pandas as pda
import numpy as npy
'''
fname = r"D:\Python36\Lib\site-packages\data\machine_learning_2_7\test_2_7\test_film.csv"
data = pda.read_csv(fname)
data2 = data.T #转置
heigh = data2.iloc[1,:5].values #第2行前5列取值，确定柱子高度
pos=npy.arange(5)+0.75 #位置表示中心点距离原点的距离,一般+i的i=arange的step
fig,ax = plt.subplots() #两个方法取第二个 ax.bar:竖柱状图 ax.barh:横柱状图
ax.barh(pos,heigh,0.3) #柱状图参数：位置，高度，大小[0-1的小数，越小越细]
ax.set_yticks(range(1,6)) #x轴的刻度尺
ax.set_yticklabels(list('QWERT'),rotation=45) #横坐标依次倾斜显示
ax.set_xlabel('look') #横竖显示的时候，注意修改对应轴的刻度尺,如xticks改成yticks
ax.set_ylabel('no run')
ax.set_title('Result')
plt.show()
'''
'''
fig = plt.figure(figsize=(8,6),dpi=100)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
a = npy.random.random(100)
b = npy.random.random(100)
ax1.scatter(a,b)#对于同一种事物，不同媒体给出不同评分。
ax1.set_xlabel('Come on')
ax1.set_ylabel('Raaton')
ax1.set_title('Dataum')
ax2.scatter(b,a)
ax2.set_title('Where')
ax2.set_xlabel('Raaton')
ax2.set_ylabel('Come on')
plt.show()
'''
'''
#fig,ax = plt.subplots() 
fig = plt.figure(figsize=(8,6),dpi=100)
ax1 = fig.add_subplot(4,1,1)#bins表示柱子数目
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)
ax1.hist(50*npy.random.random(100),range=(0,5),bins=20)#第二个参数range=(3,5)
ax1.set_title('Distributed')
ax1.set_ylim(0,50)
ax2.hist(npy.random.random(100),10,range=(0,5))#第二个参数range=(3,5)
ax2.set_title('Asked ')
ax2.set_ylim(0,50)
ax3.hist(20*npy.random.random(100),20,range=(0,5))#第二个参数range=(3,5)
ax3.set_title('Bround')
ax3.set_ylim(0,50)
ax4.hist(10*npy.random.random(100),20,range=(0,5))#第二个参数range=(3,5)
ax4.set_title('Country')
ax4.set_ylim(0,50)
plt.show()
'''
'''
fig,ax=plt.subplots()
ax.boxplot(5*npy.random.random(20)) #盒图:四分图，表示1/4数据量，宽：散乱 窄：集中
ax.set_xticklabels(['Userful'])
ax.set_ylim(0,5)
plt.show()
'''
num_columns = ['','','','']#四个列名
fig,ax = plt.subplots()#一张图中显示多个盒子图形
ax.boxplot(data[num_columns].values)
#ax.tick_params(bottom='off',top='off',left='off',right='off') 去掉框上的小齿痕
ax.set_xticklabels(num_columns,roration=90)#横坐标标出名称，旋转角度
ax.set_ylim(0,5)
plt.show()




