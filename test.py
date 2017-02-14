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
