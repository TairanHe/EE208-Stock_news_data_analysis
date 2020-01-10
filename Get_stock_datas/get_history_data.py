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

'''
获取历史行情数据 get_hist_data()

获取个股历史交易数据（包括均线数据），可以通过参数设置获取日k线、周k线、月k线，以及5分钟、15分钟、30分钟和60分钟k线数据。本接口只能获取近3年的日线数据，适合搭配均线数据进行选股和分析。

参数说明：

code：股票代码，即6位数字代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
start：开始日期，格式YYYY-MM-DD
end：结束日期，格式YYYY-MM-DD
ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
retry_count：当网络异常后重试次数，默认为3
pause:重试时停顿秒数，默认为0
返回值说明：

date：日期
open：开盘价
high：最高价
close：收盘价
low：最低价
volume：成交量
price_change：价格变动
p_change：涨跌幅
ma5：5日均价
ma10：10日均价
ma20:20日均价
v_ma5:5日均量
v_ma10:10日均量
v_ma20:20日均量
turnover:换手率[注：指数无此项]
'''


history = list()
codes = read_Astocks_data("code")
dates = ['2020-01-10', '2020-01-09','2020-01-08', '2020-01-07','2020-01-06', '2020-01-03','2020-01-02', '2019-12-31', '2019-12-30', '2019-12-27','2019-12-26','2019-12-25','2019-12-24','2019-12-23','2019-12-20','2019-12-19','2019-12-18','2019-12-17','2019-12-16','2019-12-13','2019-12-12','2019-12-11','2019-12-10']
# i=0
for code in tqdm(codes):
    # i=i+1
    # if i>5: break
    try:
        line = [code]
        history.append(line)
        hist_data = ts.get_hist_data(code,ktype="D",start="2019-12-10",end="2020-1-10",retry_count=10)
        open = hist_data['open'].tolist()
        low = hist_data['low'].tolist()
        high = hist_data['high'].tolist()
        close = hist_data['close'].tolist()
        # print(open[0])
        #
        # print(len(dates))
        # print(len(open))
        for i in range(0, min(len(dates),len(open))):
            line = []
            line.append(dates[i])
            line.append(open[i])
            line.append(low[i])
            line.append(high[i])
            line.append(close[i])
            history.append(line)

        history.append([" "])
    except:
        continue

print(history)
# open_file_and_save("../Data/stocks/history.csv",history)


# with open('../Data/stocks/history.csv', 'w', newline='') as csvfile:
#     writer  = csv.writer(csvfile)
#     for row in history:
#         writer.writerow(row)

data_write_csv('../Data/stocks/history.csv',history)


