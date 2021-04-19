#第一部分
#coding:utf-8
import sys
import logging
import time
import datetime
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt

from optparse import OptionParser
# 在jpythonbook时，需要添加下面的语句
#%matplotlib inline
from mpl_toolkits.mplot3d import Axes3D
import itertools
import os
import re
from collections import defaultdict

#输入需要画的column名中间的分隔符
KsplitTag=","

FIG_STYLE="bmh"

matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['SimHei'] + matplotlib.rcParams['font.sans-serif']
matplotlib.rcParams['axes.unicode_minus'] = False

matplotlib.style.use(FIG_STYLE)
FIG_SIZE=(10,8)
FIG_DPI=150



def HandleFile(file_name, new_index_column, draw_column_list):
    if not os.path.exists(file_name) \
            or not os.path.isfile(file_name):
        logging.info("file {0} don't exist or is not a file".format(file_name))
        return False, None
    # 第二部分
    # 将csv文件内容读到Datas 这个list
    # test.csv是由excel文件转化为csv的，文件中的datetime字段为常规类型，为YYmmddHHMMSS格式
    # parse_dates表示让pd将此字段转为日期格式 YY-mm-dd HH:MM:SS
    # usecols表示只需要读取的列名
    df =pd.DataFrame()
    new_index = new_index_column.strip()
    #将draw_column_list转为加双引号的列表
    colum_list = []
    if KsplitTag in draw_column_list:
        colum_list = draw_column_list.strip().split(',')
    else:
        colum_list.extend("{0}".format(draw_column_list))
    try:

        if new_index == '':
            #不需要设置新的column为index
            df = pd.read_excel(file_name, columns=colum_list)
        else:
            colum_list.extend("{0}".format(new_index))
            df = pd.read_excel(file_name, columns=colum_list)
    except IOError:
        print("open excel file {0} error!".format(file_name))
        return False, None

    # 删除所有有空的单元格的行
    print("begin to delete row which include any NULL unit.")
    df.dropna(axis=0, how="any", inplace=True)

    # 如果有时间的字段，设置它为index
    if new_index != "":
        df.sort_values(new_index, ascending=True, inplace=True)
        df.set_index(new_index, inplace=True)

    return True,df

    # 将一个二维表转为一个二列的表，其中第一列为时间，第二列为一个二维表
    '''
    for n in range(len(datetimes)):
        # pd.DataFrame生成一个二维表格，列名为columns设置，且自动生成一个列索引，
        # print(internal_latency.loc[[n]])
        print(pd.DataFrame(internal_latency.loc[[n]], columns=['id', 'num']))
        # 将每一行的这个列表，再加上时间
        datas.extend([('%02d:%02d:%02d' % (datetimes[n].hour, datetimes[n].minute, datetimes[n].second),
                       pd.DataFrame(internal_latency.loc[[n]], columns=['id', 'num'])), ])
    '''

def DrawPic(df, x_lable="", y_label=""):
    print("begin to draw picture")
    fig = plt.figure(figsize=FIG_SIZE, dpi=FIG_DPI)
    #只设置一个画布
    ax = fig.add_subplot(111)
    df.plot(ax=ax, marker='o', linestyle='-', markersize=6)

    ax.set_ylabel(y_label)
    plt.xlabel(x_lable)
    #plt.minorticks_on()
    #plt.grid()
    #ax.legend(loc='upper center', ncol=len(df.columns), bbox_to_anchor=(0.5, 1.10))
    plt.savefig("./summary.png")
    plt.close()
    return True

def HandleData(file_name,
            new_index_column,
            draw_column_list):
    ret, df = HandleFile(file_name, new_index_column, draw_column_list)
    if not ret:
        return False
    return DrawPic(df)

#暂时通过输入参数的形式，对外提供生成多种形式的图
def main():
    parser = OptionParser(
        usage=u"%prog <input_excel_file> <index_column> <draw_column_list>",
        description=u"generator picture file",
        version=""
    )
    # 增加必要的选项信息
    parser.add_option("-s", "--input_file",action=u'store',dest="input_excel_file",help="input excel file")
    parser.add_option("-i", "--index_column", action=u'store', default="", dest="index_column", help="select a new column as index column")
    parser.add_option("-c", "--draw_column_list", action=u'store', dest="draw_column_list", help="select a column to draw")

    (options, args) = parser.parse_args()
    print("{0}, {1}, {2}".format(options.input_excel_file,
                                 options.index_column,
                                 options.draw_column_list))

    if not options.input_excel_file \
            or not options.index_column \
            or not options.draw_column_list:
        sys.stderr.write("Error:<input_excel_file> <draw_column_list> is missing\n")
        parser.print_help(sys.stderr)
        sys.exit(2)
    log_format = u"%(asctime)s %(levelname)s %(funcName)s %(lineno)d %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_format)
    logging.info(u"begin to parse file {0}".format(options.input_excel_file))
    if not HandleData(options.input_excel_file,
        options.index_column,
        options.draw_column_list):
        sys.exit(2)
    logging.info(u"success")

if __name__ == "__main__":
    main()