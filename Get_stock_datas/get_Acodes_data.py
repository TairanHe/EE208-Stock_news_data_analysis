import tushare as ts
import pandas as pd
import numpy as np
from Tools.read_write import *


# noinspection PyTypeChecker
def open_file_and_save(file_path, data):
    """
    :param file_path: type==string
    :param data:
    """
    try:
        with open(file_path, 'ab') as f_handle:
            np.savetxt(f_handle, data, fmt='%s')
    except FileNotFoundError:
        with open(file_path, 'wb') as f_handle:
            np.savetxt(f_handle, data, fmt='%s')


stocks = pd.read_csv("../Data/stocks/Astocks.csv",sep=' ',dtype={'code':str})
codes = stocks['code'].tolist()
print(codes)
print(type(codes))
open_file_and_save("../Data/stocks/Acodes.csv", codes)
exit(0)



