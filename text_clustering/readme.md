# 文本聚合
关于文本聚合代码的说明
## `make_pre_file.py`
将位于`Data/news/html`中的网页文件整合成一份文件，每张网页内容单独成一行
### 注意事项
这一部分的代码文件用到了绝对路径，不知道在GitHub上能否成功运行。
## `cluster_by_Kmeans.py`
将整合好的文件放入Kmeans算法中聚合。代码中`n_clusters`表示了期望的聚合堆数。
## `get_key_words.py`
将聚合后的每堆文件进行处理，提取关键词语。

## a new way: 直接聚合分类

## 面对的问题：网页太多，速度太慢。同时接口不明确。
maybe：缩减需要聚类的网页