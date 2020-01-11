# 文本聚合
关于文本聚合代码的说明

#老版本部分，可以不看
#### `make_pre_file.py`
将位于`Data/news/html`中的网页文件整合成一份文件，每张网页内容单独成一行
#### `cluster_by_Kmeans.py`
将整合好的文件放入Kmeans算法中聚合。代码中`n_clusters`表示了期望的聚合堆数。
#### `get_key_words.py`
将聚合后的每堆文件进行处理，提取关键词语。

# 推荐使用
## a new way: 直接聚合分类——`get_cluster_directly.py`
为了加快速度，我只取了html文件夹中的前300条记录作为分词依据as demo。

文件打印出聚合后每组的关键字词。

要获取分组后每组的网页内容和原网址：

result字典中key值代表分好的堆编号；value值是一个数组。访问堆内的新闻文件：
```angular2html
for k,v in result.item():
    for num in v:
        filename = files[num]
```
访问堆内新闻的原网址：

拿到filename后在index.txt中查找对应网址
## 面对的问题：网页太多，速度太慢。同时接口不明确。
maybe：缩减需要聚类的网页