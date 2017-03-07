#coding:utf-8

import time
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
%matplotlib inline # 用于将图相钳到notebook中

FIG_STYLE="bmh"
#print plt.style.available
matplotlib.style.use(FIG_STYLE)
FIG_SIZE=(10,8)
FIG_DPI=150

def describe(a):
    return pd.Series({
    'count': len(a),
    'max': a.max(),
    'std': a.std(),
    'mean': a.mean(),
    '50%': np.percentile(a, 50),
    '90%': np.percentile(a, 90),
    })

#用表格统计latency值在不同段的分布
def getSummary():
    summary = pd.DataFrame()
    for name, data in datas:
        s = describe(data['Latency'])
        s.name = name
        summary = summary.append(s)
        summary = summary[['count','max','std','mean','50%','90%']]
     summary
            
 #给下面summary进行画图
 def drawSummary():
    fig=plt.figure(figsize=FIG_SIZE, dpi=FIG_DPI)
    ax=fig.add_subplot(111)
    summary.drop(['count','max','min'], axis=1).plot(ax=ax, market='o')
    plt.ylabel("microseconds")
    plt.minorticks_on()
    ax.legend(loc='upper center', ncol=len(summary.columns), bbox_to_anchor=(0.5, 1.10))
    plt.savefig("summary.png")
            
            
#设置datas的值 
def setDatas():            
    tmp=list()
    for n in range(10):
        tmp.append(pd.DataFrame(internal[interanl['XX']==10], columns=['aa','bb']))
        datas.extend([
                    ('abc', tmp[n][['aa','bb']])，
        ])
            
           
#对于需要进行分组处理的图，如需要显示1秒（分成10分），每分内各种属性的点有多少个
def analysis_group_data():
    fig=plt.figure(figsize=FIG_SIZE, dpi=FIG_DPI)
    ax=fig.add_subplot(111)    
    plt.minorticks_on()
    
    #usecols指定只加载的列
    internal=pd.read_csv('file.csv', parse_dates=True, usecols=['datetime','name','age'])
    internal=internal[internal['age'].astype(np.int32) < 100] #astype指定数据类型, 并用[[]] 来指定选择数据，可以用&连接多个条件
    internal['datetime']=pd.to_datetime(internal['datetime'],utc=8)
    #也可以不需要转为数字 
    print internal['datetime'].dt.microsecond #直接得到想要的部分
   
    internal['datetime']=internal['datetime'].astype(np.int64) #将时间转为数字
    #可以直接转为数字 ，也可以看时间只包含多少个毫秒之类的internal['MDSnapshortTime_r'].dt.minute/pd.Timedelta('1us')
    
    min=internal['datetime'].min()
    addnoe=pd.Series([cla(x) for x in internal.datetime])
    internal=internal.reset_index(drop=True)#有可能用户只是取了internal中的一部分 ，则它的index不一定是从0开始的，这时如果增加一列，会报错
    internal['aadone']=aadone #增加一列
    def cla(n):
        return '%d'%((n-min)/lim) #将某一列按一个规则进行等分
    
    groups=internal.groupby(['datetime','name']) #分组
    tmp=groups['age'].agg([‘num’, 'count']) #对于列age ,进行统计并设置一个新的列，叫num
    
    num_list=pd.unique(tmp.index.get_level_values(0))
    for num in num_list:
        data=tmp.loc[num]#得到某一组下的数据
        ax.plot(data, label=num, market='.', linestyle='', markersize=6) #linestype用于表示是用连线‘-’，markersize表点的大小
    ax.legend(loc='upper right', ncol=(len(num_list)+1)/5) #loc表示label写在什么方向，ncol表示要显示为多少列
            
def opencsvfile():
    internal=pd.read_csv('xx.csv', parse_dates=True)
    internal['MDSnapshortTime_r']=pd.to_datetime(internal['MDSnapshortTime_r']) #XX.csv中的这行为一个包含日期与时间的数字，这样的话系统自动识别
    #它，将将它转为matlab的日期时间格式，并且可以拿它做为x轴的坐标

            
            
            
def drawpicture():
    fug,ax = plt.subplots()            
    fig=plt.figure(figsize=FIG_SIZE, dpi=FIG_DPI)
    ax=fig.add_subplot(111)
    i=0
    for label, data in datas:
        ax.plot(np.arange(list(np.arange(int(summary.loc['%d'%datetime[i], 'count']))),
        data['Latency'],
        label=label, marker='.' , linestyple='', markersize=2)
        i=i+1
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=10)
    plt.ylabel(u'microseconds')
    plt.xlabel('snap')
    plt.minorticks_on()
    #plt.ylim(0, 5000)
    ax.legend(loc='best', markerscale=5)
    plt.savefig('latency.png')
                
#行列均进行应用
 def colAndline():
    def num_missing(x):    
        return sum(x.isnull())  #Apply到每一列:  
    print "Missing values per column:"  
    print data.apply(num_missing, axis=0) #axis=0代表函数应用于每一列  
    #Apply到每一行:  
    print "nMissing values per row:" 
    print data.apply(num_missing, axis=1).head() #axis=1代表函数应用于每一行 
                                
                                
def test():
    xticks = list(set(data['DateTime']))
    xticklables=["%4d-%2d-%2d %2d:%2d:%2d" %(time.strptime(str(n)[0:-3], "%Y%m%d%H%M%S").tm_year,
        time.strptime(str(n)[0:-3], "%Y%m%d%H%M%S").tm_mon,
        time.strptime(str(n)[0:-3], "%Y%m%d%H%M%S").tm_mday,
        time.strptime(str(n)[0:-3], "%Y%m%d%H%M%S").tm_hour,
        time.strptime(str(n)[0:-3], "%Y%m%d%H%M%S").tm_min,
        time.strptime(str(n)[0:-3], "%Y%m%d%H%M%S").tm_sec) for n in list(set(data['DateTime']))]

    #散列点
    plt.scatter(data['DateTime'], data['Latency'])

    #任务形状来画图,第三个参数来进行选择各种图形，现在用的是点
    #ax.plot(data['DateTime'], data['Latency', "."])
    #汉字不一定能显示出来
    plt.ylable(u'时延')

    ax.set_xticks(xticks)
    ax.set_xticklables(xticklables, rotation=15)



    plt.savefig('./a.png', format='png')
plg.close()
