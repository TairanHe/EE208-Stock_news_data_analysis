import sys, os, lucene

from java.io import File
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory, MMapDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.util import Version
from java.nio.file import Paths
from org.apache.lucene.analysis.cn.smart import SmartChineseAnalyzer


def run(searcher, analyzer, command):
    query = QueryParser("contents", analyzer).parse(command)
    scoreDocs = searcher.search(query, 50).scoreDocs
    ans = []
    for i, scoreDoc in enumerate(scoreDocs):
        doc = searcher.doc(scoreDoc.doc)
        ans.append({'start': doc.get("start"), 'name': doc.get("stocksname"),
                    'url': doc.get("url"), 'title': doc.get("title"),
                    'sum': doc.get("sum"), 'content':doc.get('contents')})

    return ans


def search(command):
    STORE_DIR = "index"
    # base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    directory = MMapDirectory(Paths.get(STORE_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = SmartChineseAnalyzer()
    ans = run(searcher, analyzer, command)
    del searcher
    return ans

# vm_env = lucene.initVM(vmargs=['-Djava.awt.headless=true'])
# for y in search('二三四五'):
#     print(y)