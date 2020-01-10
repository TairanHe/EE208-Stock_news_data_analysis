# 用Tushare获取股票数据
结果显示代表
```
    code,代码  name,名称  industry,所属行业   area,地区   pe,市盈率   outstanding,流通股本(亿)   totals,总股本(亿)   totalAssets,总资产(万)   liquidAssets,流动资产

    fixedAssets,固定资产   reserved,公积金   reservedPerShare,每股公积金   esp,每股收益   bvps,每股净资   pb,市净率   timeToMarket,上市日期

    undp,未分利润   perundp, 每股未分配   rev,收入同比(%)   profit,利润同比(%)   gpr,毛利率(%)   npr,净利润率(%)   holders,股东人数
    
```






# Get_stock_datas 获得股票信息
## `get_Astocks_data.py`
不要运行，该文件导出的`Astocks.csv`不可直接使用，运行此文件可能导致数据损坏

该文件导出的`Astocks.csv`中有很多名字为三个字的股票如`五粮液`实际数据形式为`五 粮 液`,需要进行修改

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

## `get_history_data`
该文件用于生成A股所有代码近一个月以来的股价信息并存入`history.csv`
