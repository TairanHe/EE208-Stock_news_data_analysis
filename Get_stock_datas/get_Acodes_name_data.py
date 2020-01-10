import tushare as ts
import pandas as pd
import numpy as np

# b = np.genfromtxt("../Data/A_stocks_name_code.csv")
# # a = np.recfromcsv("../Data/A_stocks_name_code.csv")
# # print(a[0][0])
# print(b)

#print(stocks)
#print(stocks[3])
# data = ts.get_hist_data('600848')
# print(data[0:5])

# noinspection PyTypeChecker
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


stocks = pd.read_csv("../Data/stocks/Astocks.csv",sep=' ',dtype={'code':str})
codes = stocks['code'].tolist()
names = stocks['name'].tolist()
print(names)
codes_names = []
for i in range (0, len(codes)):
    codes_names.append([codes[i],names[i]])
print(codes_names)

open_file_and_save("../Data/stocks/Acodes_names.csv", codes_names)
exit(0)
# print(symbols['code'][0:5])
# print(symbols.index)
# exit(0)
stocks = ts.get_stock_basics()
symbols = stocks.index.tolist()
# print(type(all_stock))
# # print(all_stock[0])
# all_stock = np.array(all_stock)
# all_stock = [1,2,3,4,5]
symbols.to_csv("../Data/Acodes")

# np.savetxt("../Data/symbols",int(all_stock))


