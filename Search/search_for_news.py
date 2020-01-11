#!/usr/bin/env python

INDEX_DIR = "IndexFiles.index"

import sys, os, lucene
from gol import *

from java.io import File
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.util import Version
from java.nio.file import Paths
from org.apache.lucene.analysis.cn.smart import SmartChineseAnalyzer

"""
This script is loosely based on the Lucene (java implementation) demo class 
org.apache.lucene.demo.SearchFiles.  It will prompt for a search query, then it
will search the Lucene index in the current directory called 'index' for the
search query entered against the 'contents' field.  It will then display the
'path' and 'name' fields for each of the hits it finds in the index.  Note that
search.close() is currently commented out because it causes a stack overflow in
some cases.
"""
def run(searcher, analyzer,command):
    # while True:
        # print()
        # print("Hit enter with no input to quit.")
        # command = input("Query:")
    command = str(command)
    print("your command:",command)
    if command == '':
        return

    # print()
    # print("Searching for:", command)
    query = QueryParser("contents",analyzer).parse(command)
    scoreDocs = searcher.search(query, 100).scoreDocs
    totalnum = len(scoreDocs)
    results = []
    for i, scoreDoc in enumerate(scoreDocs):
        doc = searcher.doc(scoreDoc.doc)
        result = {}
        result['title'] = doc.get("title")
        print(result['title'])
        flag =False
        for past in results:
            if(past['title'] == result['title']):
                totalnum -= 1
                flag = True
                break
        if(flag):
            break
        result['url'] = doc.get("url")
        result['Acodes'] = doc.get("Acodes")
        result['Stockname'] = doc.get("Stockname")
        # result['relative'] = findrelative(doc.get("path"),command)
        result['relative1'] = findrelative1(doc.get("path"),command)
        result['relative2'] = findrelative2(doc.get("path"), command)
        results.append(result)
    return totalnum,results
        # print 'explain:', searcher.explain(query, scoreDoc.doc)

def findrelative1(filepath,command):
    with open(filepath,'r') as f:
        contents = f.read()
        sub = contents.index(command)
        if sub>20:
            return "……"+contents[sub-20:sub]
        else:
            return contents[:sub]

def findrelative2(filepath,command):
    length = len(command)
    with open(filepath,'r') as f:
        contents = f.read()
        sub = contents.index(command)
        return contents[sub+length:sub+20]+"……"

def searchResults(command):
    STORE_DIR = "index"
    vm_env = getenv()
    try:
        vm_env = lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    except:
        vm_env.attachCurrentThread()
    directory = SimpleFSDirectory(Paths.get(STORE_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = SmartChineseAnalyzer()
    num,results = run(searcher, analyzer, command)
    del searcher
    return num,results

# if __name__ == '__main__':
#     STORE_DIR = "index"
#     vm_env = getenv()
#     try:
#         vm_env = lucene.initVM(vmargs=['-Djava.awt.headless=true'])
#     except:
#         vm_env.attachCurrentThread()
#     print('lucene', lucene.VERSION)
#     #base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
#     directory = SimpleFSDirectory(Paths.get(STORE_DIR))
#     searcher = IndexSearcher(DirectoryReader.open(directory))
#     analyzer = SmartChineseAnalyzer()
#     command = input("Query:")
#     num,results = run(searcher, analyzer,command)
#     print(num)
#     for result in results:
#         print(result['url'])
#         print(result['Acodes'])
#         print(result['Stockname'])
#         print(result['relative1'])
#         print(result['relative2'])
#     del searcher