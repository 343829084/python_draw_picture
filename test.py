#coding:utf-8

import time
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
%matplotlib inline # 用于将图相钳到notebook中

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
def show_dataFrame():
            summary = pd.DataFrame()
            for name, data in datas:
            s = describe(data['Latency'])
            s.name = name
            summary = summary.append(s)
            summary = summary[['count','max','std','mean','50%','90%']]
            print summary

data=pd.read_csv(r'tcp.csv')
fug,ax = plt.subplots()

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
