# noinspection PyTypeChecker
import numpy as np
import pandas as pd
import tushare as ts

# 输出一个包含文件每行内容的列表
def read_file(file_path):
    data_set = []
    with open(file_path,encoding='UTF-8') as f:
        line = f.readline()
        data_set.append(line)
    return data_set

# 通过股票编码查找股票名称
def find_name(codes):
    with open('../Data/stocks/Acodes_names.csv',encoding='UTF-8') as f:
        while True:
            line = f.readline()
            sup = line.index(' ')
            if(codes == line[:sup]):
                return line[sup+1:]

def find_number(name):
    with open('../Data/stocks/Acodes_names.csv', encoding='UTF-8') as f:
        while True:
            line = f.readline().strip()
            tmp = line.index(' ')
            if(name == line[tmp+1:]):
                return  line[:tmp]

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

