import tushare as ts
import pandas as pd
import numpy as np



stocks = ts.get_stock_basics()


##不要运行！！！！
stocks.to_csv("../Data/stocks/Astocks_2.csv")



