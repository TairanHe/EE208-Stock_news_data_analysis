# EE208-Stock_news_data_analysis
Final homework for EE208 aiming for analyze stock datas and news.

Let's get started!
# Data文件夹用于存储所有数据
## `Data/figures`
## `Data/news`
`html`文件夹存储网页新闻：

1、每个文件起始行为原网页标题。

2、每支股票爬取10条最新新闻，其文件命名末尾六位数字代表其股票编号。

`index.txt`文件包含了html文件夹中网页源码文件与原网址的关系：
格式为 ‘原网址’ + ‘，’ + ‘文件名’
## `Data/stocks`
结果显示代表
```
    code,代码  name,名称  industry,所属行业   area,地区   pe,市盈率   outstanding,流通股本(亿)   totals,总股本(亿)   totalAssets,总资产(万)   liquidAssets,流动资产

    fixedAssets,固定资产   reserved,公积金   reservedPerShare,每股公积金   esp,每股收益   bvps,每股净资   pb,市净率   timeToMarket,上市日期

    undp,未分利润   perundp, 每股未分配   rev,收入同比(%)   profit,利润同比(%)   gpr,毛利率(%)   npr,净利润率(%)   holders,股东人数
    
```

stocks 文件用于存储A股中所有股市的信息，注意，`Astocks.csv` 文件是一切的根基，这个文件是经过了很多转换和手工清洗操作的，不要随意更改

`Acodes.csv`和`Acodes_names.csv`可以从`Astocks.csv`中处理而得，更多代码细节在`Get_stock_datas`中展示

# Get_stock_datas 获得股票信息
获得数据在 `Data/stocks` 中

代码细节请见 `Get_stock_datas` 中的`README.md`

# Tool工具函数

需要重复使用的工具函数放在这里
## `read_write.py`
### `def open_file_and_save(file_path, data):`
用于将列表数据data（支持一维列表和二维列表）写成csv文件保存

# 文本聚类
具体详见`text_clustering`文件夹

# 评论分析
check /stock_recommendation_spider
Forked from [https://github.com/Jasonbaby/stock_recommendation_spider]


# 优秀资源汇总
## git入门安装使用指南
   [https://blog.csdn.net/qq_41782425/article/details/85370032]
## git官方指南
   [https://help.github.com/cn/github]
## 可能对git的ssh配置有帮助
#### 需要先从git官网上下一个git
   [https://blog.csdn.net/JT_WPC/article/details/90607049]
 
