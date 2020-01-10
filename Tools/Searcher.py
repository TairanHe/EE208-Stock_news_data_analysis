# noinspection PyTypeChecker

import numpy as np
import pandas as pd
#import tushare as ts
from Tools.read_write import *


class Searcher:
    def __init__(self, path='../Data/stocks/Astocks.csv'):
        self.stocks = into_list(path=path)

    def get_full_info_by_code(self, code):
        for index in range(0, len(self.stocks)):
            if self.stocks[index][0] == code:
                return self.stocks[index]
        raise Exception("Invalid code! 何泰然号Searcher 搜索不到～")

    def get_name(self, code): # 名称
        info = self.get_full_info_by_code(code)
        return info[1]

    def get_industry(self, code): # 所属行业
        info = self.get_full_info_by_code(code)
        return info[2]

    def get_area(self, code): # 地区
        info = self.get_full_info_by_code(code)
        return info[3]

    def get_pe(self, code): # 市盈率
        info = self.get_full_info_by_code(code)
        return info[4]

    def get_outstanding(self, code): # 流通资本（亿）
        info = self.get_full_info_by_code(code)
        return info[5]

    def get_totals(self, code): # 总股本（亿）
        info = self.get_full_info_by_code(code)
        return info[6]

    def get_totalAssets(self, code): # 总资产（万）
        info = self.get_full_info_by_code(code)
        return info[7]

    def get_liquidAssets(self, code): # 流动资产
        info = self.get_full_info_by_code(code)
        return info[8]

    def get_fixedAsserts(self, code): # 固定资产
        info = self.get_full_info_by_code(code)
        return info[9]

    def get_reserved(self, code): # 公积金
        info = self.get_full_info_by_code(code)
        return info[10]

    def get_reservedPerShare(self, code): # 每股共积金
        info = self.get_full_info_by_code(code)
        return info[11]

    def get_esp(self, code): # 每股收益
        info = self.get_full_info_by_code(code)
        return info[12]

    def get_bvps(self, code): # 每股净资
        info = self.get_full_info_by_code(code)
        return info[13]

    def get_pb(self, code): # 市净率
        info = self.get_full_info_by_code(code)
        return info[14]

    def get_timeToMarket(self, code): # 上市日期
        info = self.get_full_info_by_code(code)
        return info[15]

    def get_undp(self, code): # 未分利益
        info = self.get_full_info_by_code(code)
        return info[16]

    def get_perundp(self, code): # 每股未分配
        info = self.get_full_info_by_code(code)
        return info[17]

    def get_rev(self, code): # 收入同比（%）
        info = self.get_full_info_by_code(code)
        return info[18]

    def get_profit(self, code): # 利润同比（%）
        info = self.get_full_info_by_code(code)
        return info[19]

    def get_gpr(self, code): # 毛利率（%）
        info = self.get_full_info_by_code(code)
        return info[20]

    def get_npr(self, code): # 净利润率（%）
        info = self.get_full_info_by_code(code)
        return info[21]

    def get_holders(self, code): # 股东人数
        info = self.get_full_info_by_code(code)
        return info[22]



#
# # test class
# if __name__ == '__main__':
#     s = Searcher()
#     name = s.get_industry("300242")
#     print(name)
