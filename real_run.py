#第一部分
#coding:utf-8

import time
import datetime
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
# 在jpythonbook时，需要添加下面的语句
#%matplotlib inline
from mpl_toolkits.mplot3d import Axes3D
import itertools
import os
import re
from collections import defaultdict

FIG_STYLE="bmh"


matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['SimHei'] + matplotlib.rcParams['font.sans-serif']
matplotlib.rcParams['axes.unicode_minus'] = False

matplotlib.style.use(FIG_STYLE)
FIG_SIZE=(10,8)
FIG_DPI=150

def describe(a, b):
    return pd.Series({
    'count': len(a),
    'bytes': sum(b),
    'max': a.max(),
    'std': a.std(),
    'mean': a.mean(),
    '50%': np.percentile(a, 50),
    '90%': np.percentile(a, 90),
    '95%': np.percentile(a, 95),
    '99%': np.percentile(a, 99),
    })


#第二部分
# 将csv文件内容读到Datas 这个list
#test.csv是由excel文件转化为csv的，文件中的datetime字段为常规类型，为YYmmddHHMMSS格式
#parse_dates表示让pd将此字段转为日期格式 YY-mm-dd HH:MM:SS
#usecols表示只需要读取的列名

internal_latency = pd.read_excel(r'test.xlsx')

internal_latency=internal_latency[internal_latency['num']>0]

datas=list()
datetimes = sorted(list(set(internal_latency['time'])))
tmp = list()

internal_latency.sort_values(by=['time'], ascending=True)
#print(internal_latency)
#将一个二维表转为一个二列的表，其中第一列为时间，第二列为一个二维表
for n in range(len(datetimes)):
    #pd.DataFrame生成一个二维表格，列名为columns设置，且自动生成一个列索引，
    #print(internal_latency.loc[[n]])    
    print(pd.DataFrame(internal_latency.loc[[n]], columns=['id','num']))   
    #将每一行的这个列表，再加上时间    
    datas.extend([('%02d:%02d:%02d'%(datetimes[n].hour,datetimes[n].minute, datetimes[n].second), pd.DataFrame(internal_latency.loc[[n]], columns=['id','num'])),])


#第三部分
summary = pd.DataFrame()
for name, data in datas:
    print(data)
    s = describe(data['id'],data['num'])
    s.name = name
    summary = summary.append(s)
summary = summary[['bytes','count']]

fig=plt.figure(figsize=FIG_SIZE, dpi=FIG_DPI)
ax1=fig.add_subplot(212)
plt.subplots_adjust(0,0,1,1,0,0)
summary.drop(['count'], axis=1).plot(ax=ax1, marker='o', linestyle='-', markersize=6)
ax1.set_ylabel(u'时延')
plt.xlabel(u'大小')

plt.minorticks_on()
locs, labels = plt.xticks()
plt.setp(labels, rotation=20)
plt.savefig("summary.png")

#暂时通过输入参数的形式，对外提供生成多种形式的图
def main():
    pass

if __name__ == "__main__":
    main()