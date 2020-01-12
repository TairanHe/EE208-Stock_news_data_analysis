import os
from tqdm import tqdm
from Tools.read_write import *
import numpy as np

def news_finder(code,path="../Data/news/html/"):
    #print(path)
    filenames = os.listdir(path)
    targets_filename = []
    for index in range(0,len(filenames)):
        if filenames[index][-10:-4] == code:
            #print(filenames[index])
            targets_filename.append(filenames[index])
    return targets_filename

def news_reader(code,path="../Data/news/html/"):
    targets_filenames = news_finder(code,path)
    #print(targets_filenames)
    news_content = []
    for targets_filename in targets_filenames:
        news_content.append(read_file(path+targets_filename))
    return news_content



def analyzer(code,path="../Data/news/html/"):
    words_dict = {"跌停": 0.3377, "调整":0.3347, "反弹":0.123, "有望":0.087, "科技":0.125, "机会": 0.087, "今日": 0.0194, "投资": 0.2957, "新高": 0.3179,
                 "下跌": 0.3451, "涨停": -0.4321, "情况":-0.2361, "影响": -0.3902, "上市": -0.2341, "产业": -0.3039, "平台":-0.3046, "进行":-0.318}
    contents = news_reader(code,path)
    value = 0
    try:
        for news in contents:
            #print(news)
            for line in news:
                for i in range(0, len(line)-2):
                    if line[i:i+2] in words_dict:
                        value += words_dict[line[i:i+2]]
                        #print(words_dict.keys())

        if value < -2.27:
            return 1
        elif value < 3.17:
            return 2
        elif value < 8.96:
            return 3
        elif value < 16.44:
            return 4
        else:
            return 5

    except:
        return 1






import random


# if __name__ == '__main__':
#     codes = read_Astocks_data()
#     values = []
#
#     for code in tqdm(codes[0:2000]):
#         values.append(analyzer(code))
#     values = np.array(values)
#     # sorted_values = sorted(values)
#     # print()
#     # print(sorted_values[0])
#     # print()
#     # print(sorted_values[199])
#     # print()
#     # print(sorted_values[399])
#     # print()
#     # print(sorted_values[599])
#     # print()
#     # print(sorted_values[799])
#     # print()
#     # print(sorted_values[999])
#     print()
#     print("mean=",values.mean())
#     print("max=", values.max())
#     print("min=", values.min())



