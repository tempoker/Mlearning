#2018-02-08 21:18:12 开始学习pandas语法
#data = pda.read_csv(fname,encoding='gb18030')
#data.dtypes 按列显示数据类型，object为字符型
#data.head(4) 前4行数据   data.tail(3)尾三行数据
#data.shape 数据框的形式 如(3,4)表示3行4列 data.columns 显示所有列名
#s = data.columns.tolist()先把列名存在list 然后筛选以'是'开头的，最后显示
#r = [i for i in s if i.startswith('是')]  data[r]显示 r为一个list
#data.sort_values('we',ascending=False)按照某列降序排列
#w = data.sort_values('Fare',ascending=False).reset_index(drop=True)降序排列后重置索引,不添加drop=True 表示新索引+原来索引都在
#data['new'] = data['gpa']/data['gpa'].max() 标准化处理
#isnull = pda.isnull(data['Age']) 判断data中Age为null的数据，返回bool类型
#age = data['Age'] len(age[isnull])显示age中null数据个数
#good = data['Age'][isnull==False] 显示age中不是null的数据
#mean_age = sum(good)/len(good) 等价于 data['Age'].mean()
#a = data.pivot_table(index='Pclass',values='Survived',aggfunc=npy.mean)
#表示制作透视表，以index为索引，与values之间的平均值关系，输出如下
'''
        Survived
Pclass          
1       0.629630
2       0.472826
3       0.242363
'''
#b = data.pivot_table(index='Pclass',values='Age')默认是平均值
'''
              Age
Pclass           
1       38.233441
2       29.877630
3       25.140620
'''
#d = data.pivot_table(index='Embarked',values=['Fare','Survived'],aggfunc=npy.sum)
#表示以Embarked为索引，同时求出与Fare和Survived之间的关系，此处求和，默认平均值 输出如下
'''
                Fare  Survived
Embarked                      
C         10072.2962        93
Q          1022.2543        30
S         17439.3988       217
'''
#new=data.dropna(axis=0,subset=['Age','Survived']) 按行索引,丢弃Age和Survived中为nan的值
'''
def hundredth_row(column):
	hundredth_item =column.loc[99]
	return hundredth_item
data.apply(hundredth_row)   #自定义函数应用在data数据框中
'''
'''
def is_null(column):
	column_null = pda.isnull(column)
	null=column[column_null]
	return len(null)
column_nu =data.apply(is_null) #axis=0[列]默认。自定义函数：统计每列缺失值
'''
'''
def which_class(row):
	pclass=row['Pclass']
	if pda.isnull(pclass):
		return 'Unknown'
	elif pclass==1:
		return 'First Class'
	elif pclass ==2:
		return 'Second Class'
	elif pclass == 3:
		return 'Third Class'
data.apply(which_class,axis=1) 传参为行，所以axis=1 取所有行 为原始数据取别名
'''
'''
def youth(row):
	age=row['Age']  #取出每行的Age所在列，依次进行判断
	if pda.isnull(age):
		return 'Unknown'
	elif age<18:
		return 'Minor'
	else:
		return 'Adult'
age_label = data.apply(youth,axis=1) 传参为行，故axis=1[行]
data['age_label'] = age_label #构造data数据新列
out = data.pivot_table(index='age_label',values='Survived'),aggfunc=npy.mean为默认关系函数，npy.sum也行，结果如下：
           Survived
age_label          
Adult      0.381032
Minor      0.539823
Unknown    0.293785   #三类人获救的平均值
'''
#r2018-02-09 01:33:23 今天学到这里，先休息了。
#2018-02-09 13:25:24 继续学习pandas，了解到pandas最上层数据结构关系：DataFrame包含Series包含ndarray
#c = Series(data['Fare'].values,index=data['Name'].values)
#c.sort_values()——按值排序 c.sort_index()——按索引排序
#c[c>50].head()——先判断C中value > 50，结果为bool值，再挑出其中True的值，即大于50的值，取前五个。 
#c[(c>50) & (c<70)].head() 挑出其中value在[50,70]区间的值，前五个。
#a = Series(data['Fare'].values,index=data['Name'].values)
#b = Series(data['Age'].values,index=data['Name'].values)
#c = (a+b)/2 得到name为索引，(Fare+Age)*0.5为值
#film_ind = data.set_index('Fare',drop=False|True) 以Fare作为索引，False:Fare不丢弃 True:内容中丢弃Fare列
#fi = data.set_index('Name',drop=False) fi['Banfield, Mr. Frederick James':'Graham, Miss. Margaret Edith']
#对索引进行切片，此时存在两种索引形式【字符索引+序号索引】，fi[1:4]同样适用。 
#取出其中float类型数据，依次求取该指标的方差，步骤如下：
#a = types[data.types.values=='float64'] 找出其中类型为float64的所有列
#b = data[a.index]显示float64类型列的数据，其中a.index为一个list b是数据框结构
#c = b.apply(lambda x:npy.std(x),axis=1) 传参为行，对该行的每个特征求取方差







