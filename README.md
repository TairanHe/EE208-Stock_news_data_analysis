# EE208-Stock_news_data_analysis
Final homework for EE208 aiming for analyze stock datas and news.

Let's get started!
# Data文件夹用于存储所有数据
## `Data/figures`
## `Data/news`
## `Data/stocks`
结果显示代表
```
日期 ，开盘价， 最高价， 收盘价， 最低价， 成交量， 价格变动 ，涨跌幅，5日均价，10日均价，20日均价，5日均量，10日均量，20日均量，换手率

```

stocks 文件用于存储A股中所有股市的信息，注意，`Astocks.csv` 文件是一切的根基，这个文件是经过了很多转换和手工清洗操作的，不要随意更改

`Acodes.csv`和`Acodes_names.csv`可以从`Astocks.csv`中处理而得，更多代码细节在`Get_stock_datas`中展示

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

#Tool工具函数
需要重复使用的工具函数放在这里
## `read_write.py`
### `def open_file_and_save(file_path, data):`
用于将列表数据data（支持一维列表和二维列表）写成csv文件保存

# 评论分析
check /stock_recommendation_spider
Forked from [https://github.com/Jasonbaby/stock_recommendation_spider]


# 优秀资源汇总
## git入门安装使用指南
   [https://blog.csdn.net/qq_41782425/article/details/85370032]
## 可能对git的ssh配置有帮助
#### 需要先从git官网上下一个git
   [https://blog.csdn.net/JT_WPC/article/details/90607049]


#I'm huang