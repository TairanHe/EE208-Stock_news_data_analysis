import tushare as ts
import pandas as pd
import numpy as np
from Tools.read_write import *
from Tools.analyzer import *
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

    codes = read_Astocks_data()
    stars = []
    for code in tqdm(codes):
        stars.append(analyzer(code))

    codes_and_stars = []
    for i in tqdm(range(0, len(stars))):
        codes_and_stars.append([codes[i], stars[i]])
    print(codes_and_stars)

    data_write_csv('../Data/stocks/stars.csv', codes_and_stars)