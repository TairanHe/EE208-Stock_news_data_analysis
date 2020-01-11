import tushare as ts
import pandas as pd
import numpy as np
from Tools.read_write import *
from Tools.Searcher import *
from tqdm import tqdm
import csv
import codecs

def data_write_csv(file_name, datas):#file_name为写入CSV文件的路径，datas为要写入数据列表
    file_csv = codecs.open(file_name,'w+','utf-8')#追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in datas:
        writer.writerow(data)
    print("保存文件成功，处理结束")


if __name__ == '__main__':
    history = list()
    codes = read_Astocks_data("code")
    # for code in codes[0:1]:
    #     hist_data = ts.get_hist_data(code,ktype="D",start="2019-12-10",end="2020-1-10",retry_count=10)
    #     open = hist_data['open'].tolist()
    #     low = hist_data['low'].tolist()
    #     high = hist_data['high'].tolist()
    #     close = hist_data['close'].tolist()
    hist_data = ts.get_hist_data("002695", retry_count=10)
    print(hist_data)
    hist_data.to_csv("../Data/stocks/dirty_date.csv")
    #print(hist_data.iloc[0][0])
    # print(date)
    # # print(date)
    # # print(hist_data)
    # print(type(hist_data))
