# -*- coding:utf-8 -*-
import bs4
import urllib.request
import re
import urllib.parse
import os
import sys
import socket
import time
import threading
import queue
import chardet

socket.setdefaulttimeout(5)  # 设置socket层的超时时间为20秒,在read超时后能自动往下继续跑

def valid_filename(s):
    import string
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)  # 设置有效字符集
    s = ''.join(c for c in s if c in valid_chars)+'.txt'
    return s

# def getcharset(content):
#     charset = None
#     m = re.compile('<meta .*(http-equiv="?Content-Type"?.*)?charset="?([a-zA-Z0-9_-]+)"?', re.I).search(content)
#     if m and m.lastindex == 2:
#         charset = m.group(2).lower()
#     return charset

def getcharset(content):
    charset = chardet.detect(content)
    if charset['encoding'] == 'gb2312' or charset['encoding'] == 'GB2312':
        return charset['encoding']
    else:
        return 'utf-8'

def get_page(page):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    try:
        req = urllib.request.Request(page, headers=header)
        response = urllib.request.urlopen(req)
        content = response.read()
        charset = getcharset(content)
        content = content.decode(charset, 'ignore')
        response.close()
        return content
    except Exception as e:
        return None

# 提取网页中的链接
def get_all_links(content, page):
    links = []
    soup = bs4.BeautifulSoup(content, 'lxml')
    target_range = soup.find_all(attrs={'class':'datelist'})
    for target in target_range:
        for link in target.find_all('a'):
            links.append(urllib.parse.urljoin(page, link.get('href')))
        # for link in target.find('a',attrs={'href': re.compile('^http|^/')}):
        #     if link.get('href') != '/':
        #         links.append(urllib.parse.urljoin(page, link.get('href')))
    # for a in soup.findAll('a', attrs={'href': re.compile('^http|^/')}):
    #     if a.get('href') != '/':
    #         links.append(urllib.parse.urljoin(page, a.get('href')))
    return links

def working():
    global count
    while count < max_page:
        page = q.get()
        if page not in crawled:
            # if "download" in page:
            #     continue
            # if page[-4:] == ".zip" or page[-4:] == ".rar":
            #     continue
            print("NUM:", count, page)
            content = get_page(page)
            if not content:
                continue
            outlinks = get_all_links(content, page)
            stocknum = page[-12:-6] # 获取股票代码
            # 获取子页面内容
            sunnum = 0
            for link in outlinks:
                if sunnum == 10:
                    break
                content = get_page(link)
                if not content:
                    continue
                flag = add_page_to_folder(link+stocknum, content)
                sunnum += 1
            # if page in seeds: # 在目录里，获取外链，不保存页面内容
            #     content = get_page(page)
            #     if not content:
            #         continue
            #     outlinks = get_all_links(content, page)
            #     flag = 0
            #     stocknum = page[-12:-6] # 获取股票代码
            #     for link in outlinks:
            #         link = link + stocknum
            #         q.put(link)
            # else: # 已经是子页面，不获取外链，保存内容
            #     content = get_page(page[-6:])
            #     if not content:
            #         continue
            #     outlinks = []
            #     flag = add_page_to_folder(page, content)
            if varLock.acquire():
                graph[page] = outlinks
                crawled.append(page)
                varLock.release()
            if flag:
                count += 1
            if count == max_page:
                q.clear()
            q.task_done()
            time.sleep(0.2)

def clean_codes(content):
    soup = bs4.BeautifulSoup(content,'lxml')
    for script in soup(["script", "style"]):
        script.decompose()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

def add_page_to_folder(page, content):  # 将网页存到文件夹里，将网址和对应的文件名写入index.txt中
    # if not content:
    #     return
    soup = bs4.BeautifulSoup(content,'lxml')
    title = soup.find('title').get_text()
    target = soup.find(attrs={'class':'article'})
    index_filename = '../Data/news/index.txt'  # index.txt中每行是'网址 对应的文件名'
    folder = '../Data/news/html'  # 存放网页的文件夹
    filename = valid_filename(page)  # 将网址变成合法的文件名
    index = open(index_filename, 'a')
    index.write(page.encode('ascii', 'ignore').decode() + ',' + filename + '\n')
    index.close()
    if not os.path.exists(folder):  # 如果文件夹不存在则新建
        os.mkdir(folder)
    clean = clean_codes(str(target))
    if not clean:
        return 0
    # if not clean or not '\u4e00' <= clean[0] <= '\u9fff':
    #     return 0
    try:
        f = open(os.path.join(folder, filename), 'w', encoding='utf-8')
        f.write(title+'\n')
        f.write(clean)  # 将网页存入文件
        f.close()
    except Exception as e:
        print("Failed in open files:", e)
        return 0
    return 1

def clear(self):
    self.all_tasks_done.acquire()
    try:
        self.queue.clear()
        self.unfinished_tasks = 0
        self.all_tasks_done.notify_all()
    finally:
        self.all_tasks_done.release()

if __name__ == '__main__':
    queue.Queue.clear = clear

    NUM = 20
    varLock = threading.Lock()
    q = queue.Queue()
    crawled = []
    graph = {}
    seeds = []
    with open('../Data/stocks/Acodes_names.csv',encoding='UTF-8') as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            try:
                sub = line.index(' ')
            except:
                continue
            seed = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllNewsStock/symbol/sz'+line[:sub]+'.phtml'
            seeds.append(seed)

    method = 'dfs'
    max_page = 100000
    count = 0
    # q.put(seed)
    for seed in seeds:
        q.put(seed)

    for i in range(NUM):
        t = threading.Thread(target=working)
        t.setDaemon(True)
        t.start()
    q.join()
    print('done')
    print(count)