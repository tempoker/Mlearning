#2018-02-08 18:57:32 简直惊呆了，赞叹这个numpy功能齐全，昨晚九点多[2-7]开始的机器学习
import numpy as npy
a = npy.array([1,2,3,4])#创建一位数组
b = npy.array([[1,2,3],[4,5,6],[7,8,9],[12,34,56]])#创建二维数组
a.dtype #数组a的类型
b.shape #矩阵b的形式 (4,3):四行三列
b.[:,1:3] #切片，所有行and列名为‘1’和‘2’的列的数据
b == 12 #矩阵b中所有元素与12做比较，返回bool类型数据，True或False
c = (b==12) #c是一个bool类型矩阵
b[c] #返回bool数据中为true对应的值
d=(b[:,2]==6)#查询矩阵b中名为‘2’的列的所有数据是否=6，返回bool类型
#array([False,  True, False], dtype=bool)
b[d,:] #矩阵b中d=True的值所在行的所有数据 #通过列定位行
e = (b[2,:]==7)
b[:,e]#通过行定位列：定位该行为True的数据所在列 #e可以当作索引
f=((a=='1')&(a=='2')) #查询其中同时等于字符1和2的数据，返回bool值
#array([False, False, False, False], dtype=bool)
f=((a=='1')|(a=='2')) #查询其中等于字符1或者2的数据，返回bool值
#array([ True,  True, False, False], dtype=bool)
a.astype(str)#a中所有数据的类型转换为str
a.sum(axis=1)#按行求和
a.sum(axis=0)#按列求和
t = npy.arange(15).reshape(3,5)#将一维数组转换为3X5的矩阵
a.ndim #数组a的维度 此时返回1
a.size #数组a元素总数
y = npy.ones((2,3,4),dtype=npy.int32)#返回两个三行四列的list，类型为int32
'''
array([[[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]],

       [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]])
'''
npy.random.random((3,2))#随机产生一个3X2的矩阵
i = npy.linspace(0,pi*2,100)# 生成0-2×pi 100个按照等差排列的数组
#两个维度相同的int32|float类型数组，可以进行四则运算，对应位置的数据进行运算，单独幂运算也行
#两个二维数组a*b 结果是对应位置的数据进行乘法运算。
# 矩阵的乘法：a.dot(b) 等价于 npy.dot(a,b) 前提:a的列==b的行 结果是a的行数b的列数 a的每一行分别与b的每一列相乘求和
#u.reshape((6,-1)) 在指定数据个数时，需要转换为二维，只需要指定元组中一个数字即可，另一个用负数代替，系统自动计算
#a = npy.floor(10*npy.random.random((2,3))).astype(int) 随机生成10以内的小数向下取整并转换为int类型
#b = npy.floor(10*npy.random.random((2,3))).astype(int)
#c = npy.hstack((a,b)) 按行拼接   d = npy.vstack((a,b)) 按列拼接
#e = npy.arange(12).reshape(2,-1) #2X6矩阵
#npy.hsplit(e,(2,4))[vsplit(e,3)按列切分，均分为3份]表示把e按行分离，【如果是一个数字3，表示均分为3份】,元组则在索引2和4的位置分开，即[0,1] [2,3] [4,5]
#f = npy.arange(12) 1:赋值 w=f id和操作影响均是相同  2:view w=f.view() id不同，操作影响相同 3：copy r = f.copy() 完全不同
#d = npy.sin(npy.arange(1,25).reshape(8,3)) 随机生成8X3矩阵
#ind = d.argmax(axis=0) 取出每列最大值的索引 也就是最大值所在行数 结合[0,1,2]刚好定位到最大值
#data_max=d[ind,range(d.shape[1])] 得到每列最大值
#y.ravel() 将矩阵y转化为一维数组【拉伸】
#ind = d.argmax(axis=1) 取出每行最大值的索引 也就是最大值所在列数 结合range(d.shape[0])刚好定位最大值
#data_max = d[range(d.shape[0]),ind]
#a = npy.arange(0,40,10) b = npy.tile(a,(3,4)) 按照a的内容扩展为3行4列个a 如下
'''
array([[ 0, 10, 20, 30,  0, 10, 20, 30,  0, 10, 20, 30,  0, 10, 20, 30],
       [ 0, 10, 20, 30,  0, 10, 20, 30,  0, 10, 20, 30,  0, 10, 20, 30],
       [ 0, 10, 20, 30,  0, 10, 20, 30,  0, 10, 20, 30,  0, 10, 20, 30]])
'''
#b = npy.sort(s,axis=1) s=npy.array([[12,34,5],[21,5,23],[78,4,54]]) b表示将s矩阵按照行排序，默认从小到大
#s.sort(axis=1)原地将矩阵s按照行排序
#c=npy.array([2,4,3,1]) j = npy.argsort(c) j=[3 0 2 1]将c从小到大排序取其索引。c[j]按顺序取值
#2018-02-08 20:39:34 终于把第一节听完了，numpy的用法很多。
