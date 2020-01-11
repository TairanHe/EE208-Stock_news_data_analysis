
import numpy as np
import os

import pandas as pd
import tushare as ts

# 输出一个包含文件每行内容的列表


#该文件仅用于读取Astcoks.csv
def read_Astocks_data(index="code",path="../Data/stocks/Astocks.csv"):
    '''
    :param index: 你想要读取哪一列的内容，有23中数据选择：code name industry area pe outstanding totals totalAssets liquidAssets fixedAssets reserved reservedPerShare esp bvps pb timeToMarket undp perundp rev profit gpr npr holders
    对应中文是
    code,代码  name,名称  industry,所属行业   area,地区   pe,市盈率   outstanding,流通股本(亿)   totals,总股本(亿)   totalAssets,总资产(万)   liquidAssets,流动资产

    fixedAssets,固定资产   reserved,公积金   reservedPerShare,每股公积金   esp,每股收益   bvps,每股净资   pb,市净率   timeToMarket,上市日期

    undp,未分利润   perundp, 每股未分配   rev,收入同比(%)   profit,利润同比(%)   gpr,毛利率(%)   npr,净利润率(%)   holders,股东人数

    :param path: 读取Astcoks.csv对应的相对位置
    :return: 对应index的列表 [, , , , , ,  .....  , , , , , ]
    '''
    stocks = pd.read_csv(path, sep=' ', dtype={'code':str})
    results = stocks[index].tolist()
    return results

def find_news_website(file_name):
    with open('../Data/news/index.txt') as f:
        line = f.readline()
        while line:
            sup = line.index(',')
            if(file_name == line[sup+1:-1]):
                return line[:sup-6]
            line = f.readline()
    return -1

def find_news_file(website):
    with open('../Data/news/index.txt') as f:
        line = f.readline()
        while line:
            sup = line.index(',')
            if(website == line[:sup-6]):
                return line[sup+1:]
            line = f.readline()
    return -1

def read_file(file_path):
    data_set = []
    with open(file_path, encoding='UTF-8') as f:
        line = f.readline()
        while line:
            data_set.append(line)
            line = f.readline()
    return data_set


# 通过股票编码查找股票名称
def find_name(codes):
    with open('../Data/stocks/Acodes_names.csv', encoding='UTF-8') as f:
        while True:
            line = f.readline().strip()
            sup = line.index(' ')
            if codes == line[:sup]:
                return line[sup + 1:]


def find_number(name):
    with open('../Data/stocks/Acodes_names.csv', encoding='UTF-8') as f:
        while True:
            line = f.readline().strip()
            tmp = line.index(' ')
            if name == line[tmp + 1:]:
                return line[:tmp]


def open_file_and_save(file_path, data):
    """
    :param file_path: type==string
    :param data:
    """
    try:
        with open(file_path, 'ab') as f_handle:
            np.savetxt(f_handle, data, fmt='%s', encoding="utf-8")
    except FileNotFoundError:
        with open(file_path, 'wb') as f_handle:
            np.savetxt(f_handle, data, fmt='%s', encoding="utf-8")

def into_list(path='../Data/stocks/Astocks.csv'):
    with open(path, encoding='UTF-8') as f:
        ans = []
        ans = f.read().split('\n')
        ans = ans[1:]
        ans = [x.split(' ') for x in ans]
    return ans[:-1]
