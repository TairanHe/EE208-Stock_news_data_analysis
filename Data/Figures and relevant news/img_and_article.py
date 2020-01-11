import requests
from urllib import parse
from bs4 import BeautifulSoup
import urllib
import sys
import os

headers = {
    'User-Agent':'GoogleBot'
}
def clean_codes(soup):
    #for script in soup(["script", "style"]):
        #script.decompose()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text


with open('Acodes_names.csv', encoding='UTF-8') as f:
    lines = f.readlines()
    i=1000;
    while i<2000:
        try:
            with open("initurl/"+lines[i][0:6]+'.txt') as g:
                j=0
                while True:
                    url = g.readline()
                    if url == '':
                        break
                    url = url.strip()
                    #url = "https://baijiahao.baidu.com/s?id=1650793664091250269&wfr=spider&for=pc"

                    content = urllib.request.urlopen(url).read()
                    soup = BeautifulSoup(content, 'lxml')


                    #记得更新多图#已更新

                    img_container = soup.find_all("div", {"class": "img-container"})
                    if img_container:
                        os.makedirs("img_article/" + lines[i][0:6] + "/" + str(j))
                        v = 0
                        for r in img_container:
                            img = r.find("img", {"data-loadfunc": "0"})
                            try:
                                f2 = open(os.path.join("img_article/" + lines[i][0:6] + "/" + str(j), str(v) + ".jpg"),
                                          'wb')
                                f2.write((urllib.request.urlopen(img["src"])).read())
                                f2.close()
                                v += 1
                            except Exception as e:
                                continue
                    else:
                        continue
                    tmp = soup.find("div", {"class": "article-title"})
                    title = tmp.find("h2")
                    content1 = soup.find("div", {"class": "article", "id": "article"})
                    article = clean_codes(content1)


                    f1 = open(os.path.join("img_article/" + lines[i][0:6] + "/" + str(j),str(j) + '_content.txt'), 'a')
                    f1.write(url+"\n\n"+title.string + "\n\n"+article)
                    f1.close()

                    print('get ',i," ",j)
                    j+=1
                    #print(title.string)
                    #print(img["src"])
                    #print(article)
                print('finish\t',i)
                i += 1
        except Exception as u:
            print("exclude\t",i)
            i += 1
            continue