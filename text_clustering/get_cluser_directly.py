# -*- coding: utf-8 -*-

import os
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans

import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence

class KmeansClustering():
    def __init__(self, stopwords_path=None):
        self.stopwords = self.load_stopwords(stopwords_path)
        self.vectorizer = CountVectorizer()
        self.transformer = TfidfTransformer()

    def load_stopwords(self, stopwords=None):
        """
        加载停用词
        :param stopwords:
        :return:
        """
        if stopwords:
            with open(stopwords, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f]
        else:
            return []

    # 当然这里也可以直接改成每个文件一个文本
    def preprocess_data(self, files):
        """
        文本预处理，每行一个文本
        :param corpus_path:
        :return:
        """
        corpus = []
        for file in files:
            with open(path+'/'+file, 'r', encoding='utf-8') as f:
                line = f.read()
                corpus.append(' '.join([word for word in jieba.lcut(line.strip()) if word not in self.stopwords]))
        return corpus

    def get_text_tfidf_matrix(self, corpus):
        """
        获取tfidf矩阵
        :param corpus:
        :return:
        """
        tfidf = self.transformer.fit_transform(self.vectorizer.fit_transform(corpus))

        # 获取词袋中所有词语
        # words = self.vectorizer.get_feature_names()

        # 获取tfidf矩阵中权重
        weights = tfidf.toarray()
        return weights

    def kmeans(self, corpus_path, n_clusters=5):
        """
        KMeans文本聚类
        :param corpus_path: 语料路径（每行一篇）,文章id从0开始
        :param n_clusters: ：聚类类别数目
        :return: {cluster_id1:[text_id1, text_id2]}
        """
        corpus = self.preprocess_data(corpus_path)
        weights = self.get_text_tfidf_matrix(corpus)
        clf = KMeans(n_clusters=n_clusters)
        # clf.fit(weights)
        y = clf.fit_predict(weights)
        # 中心点
        # centers = clf.cluster_centers_
        # 用来评估簇的个数是否合适,距离约小说明簇分得越好,选取临界点的簇的个数
        # score = clf.inertia_
        # 每个样本所属的簇
        result = {}
        for text_idx, label_idx in enumerate(y):
            if label_idx not in result:
                result[label_idx] = [text_idx]
            else:
                result[label_idx].append(text_idx)
        return result

# 关于原数据的说明——这玩意每一行就是一条新闻
path = '../Data/news/html'
n = 7
if __name__ == '__main__':
    files = os.listdir(path)
    Kmeans = KmeansClustering(stopwords_path='stop_words.txt')
    result = Kmeans.kmeans(files, n_clusters=n)
    print(result)
    # print(type(result))

    texts = {}
    for k, v in result.items():
        text = ''
        for num in v:
            f = open('../Data/news/html/' + files[num], 'r', encoding='utf-8')
            tmp = f.read()
            tmp = tmp.strip()
            text += tmp
            f.close()
        texts[k] = text

    # 对text进行提取关键字
    for num in range(n):
        print("第%s组" % num)
        text = texts[num]
        # text = codecs.open('%s.txt' % num, 'r', 'utf-8').read()
        tr4w = TextRank4Keyword()

        tr4w.analyze(text=text, lower=True, window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象

        print('关键词：')
        for item in tr4w.get_keywords(20, word_min_len=1):
            print(item.word, item.weight)

        print()
        print('关键短语：')
        for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num=2):
            print(phrase)

        tr4s = TextRank4Sentence()
        tr4s.analyze(text=text, lower=True, source='all_filters')

    # news_data = []
    # with open('total.txt','r',encoding='utf-8') as f:
    #     line = f.readline()
    #     while line:
    #         # print(line.decode())
    #         news_data.append(line)
    #         line = f.readline()
    #
    # for k,v in result.items():
    #     f = open('%s.txt' % k,'w',encoding='utf-8')
    #     for num in v:
    #         # print(news_data[num])
    #         # print(type(news_data[num]))
    #         f.write(news_data[num])
    #     f.close()