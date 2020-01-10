# noinspection PyTypeChecker

import numpy as np
import pandas as pd
# import tushare as ts
from Tools.read_write import *


class Searcher:
    def __init__(self, path='../Data/stocks/Astocks.csv'):
        self.stocks = into_list(path=path)
        self.histories = into_list(path="../Data/stocks/history.csv")

# Searcher 为你提供了两种功能，前五个函数用于搜索股价，从第六个开始，函数用于搜索股票的综合信息
#接下来的5个函数用于搜索股票近一个月以来的股价信息
    def get_index_by_code(self, code):
        '''
        :param code:
        :return: 这个股票对应在histories中的下表索引值
        '''
        for index in range(0, len(self.histories)):
            if self.histories[index][0] == code:
                return index
        raise Exception("Invalid code! 何泰然号Searcher 搜索不到～")

    def get_date_by_code(self,code):
        index = self.get_index_by_code(code)
        index = index+1
        date=[]

        while(len(self.histories[index][0])==10): #如果是日期形式
            date.append(self.histories[index][0])
            index +=1
        return date

    def get_open_by_code(self, code):
        '''

        :param code:
        :return: 开盘股价列表
        '''
        index = self.get_index_by_code(code)
        index = index+1
        open=[]

        while(len(self.histories[index][0])==10): #如果是日期形式
            open.append(self.histories[index][1])
            index +=1
        return open

    def get_low_by_code(self, code):
        '''

        :param code:
        :return: 当天最低股价列表
        '''
        index = self.get_index_by_code(code)
        index = index + 1
        low = []

        while (len(self.histories[index][0]) == 10):  # 如果是日期形式
            low.append(self.histories[index][2])
            index += 1
        return low

    def get_high_by_code(self, code):
        '''

        :param code:
        :return: 当天最高股价列表
        '''
        index = self.get_index_by_code(code)
        index = index + 1
        high = []

        while (len(self.histories[index][0]) == 10):  # 如果是日期形式
            high.append(self.histories[index][3])
            index += 1
        return high

    def get_close_by_code(self, code):
        '''

        :param code:
        :return: 收盘股价列表
        '''
        index = self.get_index_by_code(code)
        index = index + 1
        close = []

        while (len(self.histories[index][0]) == 10):  # 如果是日期形式
            close.append(self.histories[index][4])
            index += 1
        return close




#接下来的函数用于搜索单个函数的综合数据
    def get_full_info_by_code(self, code):
        for index in range(0, len(self.stocks)):
            if self.stocks[index][0] == code:
                return self.stocks[index]
        raise Exception("Invalid code! 何泰然号Searcher 搜索不到～")

    def get_name(self, code):  # 名称
        info = self.get_full_info_by_code(code)
        return info[1]

    def get_industry(self, code):  # 所属行业
        info = self.get_full_info_by_code(code)
        return info[2]

    def get_area(self, code):  # 地区
        info = self.get_full_info_by_code(code)
        return info[3]

    def get_pe(self, code):  # 市盈率
        info = self.get_full_info_by_code(code)
        return info[4]

    def get_outstanding(self, code):  # 流通资本（亿）
        info = self.get_full_info_by_code(code)
        return info[5]

    def get_totals(self, code):  # 总股本（亿）
        info = self.get_full_info_by_code(code)
        return info[6]

    def get_totalAssets(self, code):  # 总资产（万）
        info = self.get_full_info_by_code(code)
        return info[7]

    def get_liquidAssets(self, code):  # 流动资产
        info = self.get_full_info_by_code(code)
        return info[8]

    def get_fixedAsserts(self, code):  # 固定资产
        info = self.get_full_info_by_code(code)
        return info[9]

    def get_reserved(self, code):  # 公积金
        info = self.get_full_info_by_code(code)
        return info[10]

    def get_reservedPerShare(self, code):  # 每股共积金
        info = self.get_full_info_by_code(code)
        return info[11]

    def get_esp(self, code):  # 每股收益
        info = self.get_full_info_by_code(code)
        return info[12]

    def get_bvps(self, code):  # 每股净资
        info = self.get_full_info_by_code(code)
        return info[13]

    def get_pb(self, code):  # 市净率
        info = self.get_full_info_by_code(code)
        return info[14]

    def get_timeToMarket(self, code):  # 上市日期
        info = self.get_full_info_by_code(code)
        return info[15]

    def get_undp(self, code):  # 未分利益
        info = self.get_full_info_by_code(code)
        return info[16]

    def get_perundp(self, code):  # 每股未分配
        info = self.get_full_info_by_code(code)
        return info[17]

    def get_rev(self, code):  # 收入同比（%）
        info = self.get_full_info_by_code(code)
        return info[18]

    def get_profit(self, code):  # 利润同比（%）
        info = self.get_full_info_by_code(code)
        return info[19]

    def get_gpr(self, code):  # 毛利率（%）
        info = self.get_full_info_by_code(code)
        return info[20]

    def get_npr(self, code):  # 净利润率（%）
        info = self.get_full_info_by_code(code)
        return info[21]

    def get_holders(self, code):  # 股东人数
        info = self.get_full_info_by_code(code)
        return info[22]


# # test class
# if __name__ == '__main__':
#     s = Searcher()
#     for i in range(0, 10):
#         print(type(s.histories[i][0]))
#
#
#     close = s.get_close_by_code("300591")
#     print(close)
