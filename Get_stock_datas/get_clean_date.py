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


dirty_dates = read_file("../Data/stocks/dirty_date.csv")
#print(dirty_dates)
dates = []

for i in range (1, len(dirty_dates)):
    #print(dirty_dates[i])

    line = dirty_dates[i]
    new_line = line[0:10]
    dates.append(new_line)
    print(new_line)
    #print(line)
print(dates)
open_file_and_save("../Data/stocks/dates.csv", dates)
#data_write_csv("../Data/stocks/dates.csv", dates)

