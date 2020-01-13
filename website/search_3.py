#!/usr/bin/env python

import sys, os, lucene

from java.io import File
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.util import Version
from java.nio.file import Paths
from org.apache.lucene.analysis.cn.smart import SmartChineseAnalyzer



def run(searcher, analyzer, command):

    command = str(command)
    if command == '':
        return


    query = QueryParser("contents", analyzer).parse(command)
    scoreDocs = searcher.search(query, 100).scoreDocs
    totalnum = len(scoreDocs)
    results = []
    for i, scoreDoc in enumerate(scoreDocs):
        doc = searcher.doc(scoreDoc.doc)
        result = {}
        result['title'] = doc.get("title")
        flag = False
        for past in results:
            if (past['title'] == result['title']):
                totalnum -= 1
                flag = True
                break
        if (flag):
            break
        result['url'] = doc.get("url")
        result['Acodes'] = doc.get("Acodes")
        result['Stockname'] = doc.get("Stockname")
        # result['relative'] = findrelative(doc.get("path"),command)
        with open('/media/sf_Share/'+doc.get("path"), 'r') as f:
            contents = f.read()
        result['content'] = contents
        results.append(result)
    return totalnum, results


def findrelative1(filepath, command):
    with open(filepath, 'r') as f:
        contents = f.read()
        sub = contents.index(command)
        if sub > 20:
            return "……" + contents[sub - 20:sub]
        else:
            return contents[:sub]


def findrelative2(filepath, command):
    length = len(command)
    with open(filepath, 'r') as f:
        contents = f.read()
        sub = contents.index(command)
        return contents[sub + length:sub + 20] + "……"


def searchResults(command):
    STORE_DIR = "./index_2"
    directory = SimpleFSDirectory(Paths.get(STORE_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = SmartChineseAnalyzer()
    num, results = run(searcher, analyzer, command)
    del searcher
    return results

# vm_env = lucene.initVM(vmargs=['-Djava.awt.headless=true'])
# a = searchResults('茅台')
# print(a)

