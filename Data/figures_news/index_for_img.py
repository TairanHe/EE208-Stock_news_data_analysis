#!/usr/bin/env python

INDEX_DIR = "IndexFiles.index"

import sys, os, lucene, threading, time
from datetime import datetime

from java.io import File
from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType
from org.apache.lucene.index import FieldInfo, IndexWriter, IndexWriterConfig, IndexOptions
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.util import Version
from java.nio.file import Paths
from org.apache.lucene.analysis.cn.smart import SmartChineseAnalyzer
import bs4

"""
This class is loosely based on the Lucene (java implementation) demo class 
org.apache.lucene.demo.IndexFiles.  It will take a directory as an argument
and will index all of the files in that directory and downward recursively.
It will index on the file path, the file name and the file contents.  The
resulting Lucene index will be placed in the current directory and called
'index'.
"""


class Ticker(object):

    def __init__(self):
        self.tick = True

    def run(self):
        while self.tick:
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(1.0)


class IndexFiles(object):
    """Usage: python IndexFiles <doc_directory>"""

    def __init__(self, root, storeDir):

        if not os.path.exists(storeDir):
            os.mkdir(storeDir)

        store = SimpleFSDirectory(Paths.get(storeDir))
        # analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)
        analyzer = SmartChineseAnalyzer()
        analyzer = LimitTokenCountAnalyzer(analyzer, 1048576)
        config = IndexWriterConfig(analyzer)
        # config.setOpenMode(IndexWriterConfig.OpenMode.APPEND)
        config.setOpenMode(IndexWriterConfig.OpenMode.CREATE_OR_APPEND)
        writer = IndexWriter(store, config)

        self.indexDocs(root, writer)
        ticker = Ticker()
        print('commit index', )
        threading.Thread(target=ticker.run).start()
        writer.commit()
        writer.close()
        ticker.tick = False
        print('done')

    def indexDocs(self, root, writer):

        t1 = FieldType()
        # t1.setIndexed(False)
        t1.setStored(True)
        t1.setTokenized(False)

        t2 = FieldType()
        # t2.setIndexed(True)
        t2.setStored(False)
        t2.setTokenized(True)
        # t2.setIndexOptions(FieldInfo.getIndexOptions.DOCS_AND_FREQS_AND_POSITIONS)
        t2.setIndexOptions(IndexOptions.DOCS_AND_FREQS_AND_POSITIONS)

        with open('Acodes_names.csv', encoding='UTF-8') as f:
            lines = f.readlines()
            i = 0
            while i < 100:
                number = lines[i][0:6]
            #for root, dirnames, filenames in os.walk(root):
                root = root + number + "/"
                i+=1
                files = os.listdir(root)
                for file in files:
                    #if not file.endswith('.txt'):
                        #continue
                    print("adding", file)
                    try:
                        # path = os.path.join(root, file)
                        # file = open(path)
                        # contents = unicode(file.read(), 'gbk')
                        # file.close()
                        #fileMain = open(path, "r", encoding="utf-8")
                        contents = get_imgnews_url(root,file)
                        title = get_title(root,file)
                        url = get_imgnews_url(root,file)
                        path = get_img_path(root,file)
                        #fileMain.close()

                        print("url is",url)
                        print("title:",title)
                        print("contents:",contents)
                        #print("Stockname:",Stockname)
                        doc = Document()
                        #doc.add(Field("filename", filename, t1))
                        for i in path:
                            doc.add(Field("path", i, t1))
                        doc.add(Field("title", title, t1))
                        doc.add(Field("url", url, t1))
                        # ?
                        # doc.add(Field("site", url, t2))
                        if len(contents) > 0:
                            doc.add(Field("contents", contents, t2))
                        else:
                            print("warning: no content in %s" % file)
                        writer.addDocument(doc)
                    except Exception as e:
                        print("Failed in indexDocs:", e)

# def gettitle(content):
#     if content:
#         soup = bs4.BeautifulSoup(content.replace('\n', ''), 'lxml')
#         return soup.title.string
#     return 'empty'

def get_imgnews_url(root,j):
    with open(root + str(j) + "/" + str(j) + "_content.txt") as f:
        return  f.readline().strip()
    
def get_title(root,j):
    with open(root + str(j) + "/" + str(j) + "_content.txt") as f:
        tmp = f.readlines()
        return tmp[2].strip()
    
def get_content(root,j):
    with open(root + str(j) + "/" + str(j) + "_content.txt") as f:
        tmp = f.readlines()
        return tmp[4].strip()
    
def get_img_path(root,j):
    files = os.listdir(root + str(j))
    tmp=[]
    for file in files:
        if file[-3:] == "jpg":
            tmp.append(root + str(j) + "/" + file)
    return tmp

if __name__ == '__main__':
    lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    print('lucene', lucene.VERSION)
    start = datetime.now()
    try:
        IndexFiles("img_article/", "index")
        end = datetime.now()
        print(end - start)
    except Exception as e:
        print("Failed: ", e)
        raise e