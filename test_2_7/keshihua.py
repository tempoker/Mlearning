#2018-02-09 16:48:65 开始学习数据可视化工具包matplotlib
#dt = pda.read_csv(fname)
#dt['data'] = pda.to_datetime(dt['data']) 将时间格式转化为1992-03-03
#pyl.plot(dat1['date'],dat1['rate'])
#plt.xticks(rotation=45) 当横坐标数据过长，可以倾斜显示，如45度
#plt.show()
import matplotlib.pyplot as plt
import numpy as npy
import pandas as pda
"""
fig = plt.figure(figsize=(8,6),dpi=100)# 画布的尺寸为8X6，精度为100
ax1 =fig.add_subplot(2,3,2)#分别设置三个子图
ax2 = fig.add_subplot(2,3,4)
ax3 = fig.add_subplot(2,3,6)
ax1.plot(npy.random.randint(1,5,5),npy.arange(5),'-y')#调用ax1画图
ax2.plot(npy.arange(10),npy.random.randint(1,24,10),'g')#ax2画图
plt.show()
"""
"""
#一张图内画多条线
fname = r"D:\Python36\Lib\site-packages\data\machine_learning_2_7\test_2_7\urate.csv"
data = pda.read_csv(fname) 
data['date'] = pda.to_datetime(data['date'])
fig = plt.figure(figsize=(10,6),dpi=100)
plt.plot(data[:6]['date'],data[:6]['rate'],'cp-.',label='1-6days')
plt.plot(data[6:]['date'],data[6:]['date'],'dm-',label='6-12days')
plt.xticks(rotation=60)
plt.legend(loc='best')
plt.show()
"""
"""
#折线图:一张图中循环实现多线条多标签多颜色
fig = plt.figure(figsize=(10,8),dpi=100)
colors = ['green','red','yellow','cyan']
for i in range(4):
     start_index=i*3
     end_index=(i+1)*3
     subset = data[start_index:end_index]
     label = '1945-01-'+str(i)
     plt.plot(subset['date'],subset['rate'],c=colors[i],label=label)
plt.xticks(rotation=45)
plt.legend(loc='best')
plt.xlabel('time')
plt.ylabel('rate')
plt.title('Unemployment Tend in 1945')
plt.show()
"""











