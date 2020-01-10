import os

# 将所有网页融到一个页面中来
# 按道理说这里应该放绝对路径，不知道这样在GitHub上能不能跑
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