import os

# 将所有网页融到一个页面中来
# 按道理说这里应该放绝对路径，不知道这样在GitHub上能不能跑

# 更改思路：不预处理文件，直接每个爬取的文件为原文本输入（除去第一行），Kmeans输出的是堆号和每堆文件序号
# 根据文件序号直接访问文件
# for k,v in result.items():
#     text = ''
#     for num in v:
#         f = open('../Data/news/html'+files[v],'r',encoding='utf-8')
#         f.readline()
#         tmp = f.readline()
#         text += tmp
#         f.close()
#     # 对text进行提取关键字


path ='../Data/news/html'
files = os.listdir(path)
# print(files)
with open('total.txt','w',encoding='utf-8') as f:
    for file in files:
        print(1)
        f1 = open(path+'/'+file,'r',encoding='utf-8')
        f1.readline()
        f.write(f1.read()+'\n')
        f1.close()