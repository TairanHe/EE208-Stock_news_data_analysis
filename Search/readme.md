# search文件的说明

`gol.py`用于管理JVM全局变量，方便多次查询

`search_for_news.py`文件用于作为web.py后台文件对网页内容进行查询。
## 对`search_for_news.py`输入数据的说明：
data,输入查询内容

## 对`search_for_news.py`返回数据的说明：
返回一个元组（totalnum,results）：

1、totalnum为查询到的总个数

2、results为返回的查询结果，是一个数组

results数组中的每一个元素result都为一个字典：

result['url'] 存储网页地址

result['Acodes']存储股票代码

result['Stockname']存储股票名称

result['relative1']存储左相关字段

result['relative2']存储右相关字段

在web.py中的传参例子：（我传入了totalnum,results,data三个数据）
```angular2html
<tr><td><table class = "table2" border = "1" align = center width = 90%>
	$for a in results:
		<tr><td>
		<h2>
		<a href = $a["url"]>$a["title"]</a>
		</h2>
		<h3>$a["relative1"]<em>$data</em>$a["relative2"]</h3>
		<h3><font color = "#31DFDF">$a["url"]</font></h3>
		</td></tr>
```