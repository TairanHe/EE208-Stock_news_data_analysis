# 用Tushare获取股票数据
结果显示代表
```
日期 ，开盘价， 最高价， 收盘价， 最低价， 成交量， 价格变动 ，涨跌幅，5日均价，10日均价，20日均价，5日均量，10日均量，20日均量，换手率

```






# Get_stock_datas 获得股票信息
## `get_Astocks_data.py`
不要运行，该文件导出的`Astocks.csv`不可直接使用，运行此文件可能导致数据损坏

该文件导出的`Astocks.csv`中有很多三个股票的股票如`五粮液`实际数据形式为`五 粮 液`,需要进行修改

我还将导出的csv文件的逗号`,`改成了空格` `分割，这一步有些多余，导致我们后来在用pandas读取`Astocks.csv`时需要`sep=' '`作为分割参数进行读取。

## `get_Acodes_data.py`
该文件用于生成所有A股股票的代码，并生成`Acodes.csv`

具体步骤:

1.先读取`Astocks.csv`

`stocks = pd.read_csv("../Data/stocks/Astocks.csv",sep=' ',dtype={'code':str})`

2.将Dataframe数据格式转化为list

`codes = stocks['code'].tolist()`

3.写csv文件

`open_file_and_save("../Data/stocks/Acodes.csv", codes)`

我写了一个工具函数（在`Tools/read_write.py`中）
`open_file_and_save(file_path, data):`
用于将列表写成csv文件存储

## `get_Acodes_name_data`
该文件用于生成所有A股股票的代码，并生成`Acodes_names.csv`