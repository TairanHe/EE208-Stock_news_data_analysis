import web
import random
import math
import os
import datetime
import lucene
import search_0
import search_3
import image_by_image

try:
    vm_env = lucene.initVM(vmargs=['-Djava.awt.headless=true'])
except:
    vm_env = lucene.getVMEnv()


def into_list(path='static/Astocks.csv'):
    with open(path, encoding='UTF-8') as f:
        ans = []
        ans = f.read().split('\n')
        ans = ans[1:]
        ans = [x.split(' ') for x in ans]
        for i in range(1, len(ans) - 1):
            for j in range(4, len(ans[0])):
                ans[i][j] = float(ans[i][j])
    return ans[:-1]


def into_list_2(path='static/history.csv'):
    with open(path, encoding='UTF-8') as f:
        ans = []
        ans = f.read().split('\n')
        ans = ans[1:]
        ans = [x.split(' ') for x in ans]
    return ans[:-1]


def get_star(index):
    with open('static/stars.csv', 'r') as f:
        a = f.read()
        a = a.split('\n')
        a = [x.split(' ') for x in a]
        return a[index][1]


def get_his(user):
    with open('static/user_information/{}.txt'.format(user), 'r') as f:
        ans = f.read()
        ans = ans.split('\n')
        ans = ans[:-1]
    return list(set(ans))


def get_hot():
    with open('recommand/热词.txt', 'r', encoding='gbk') as f:
        words = f.read()
        words = words.split('\n')
        return words


def get_url(i):
    with open('recommand/{}.txt'.format(str(i)), 'r') as f:
        words = f.read()
        words = words.split('\n')
        return words


def add_recom(a, user):
    if user != None:
        with open('static/user_information/{}_recom.txt'.format(user), 'a') as f:
            for x in a:
                f.write(x + '\n')
            f.write('\n')



def get_recom(user):
    if user != None:
        with open('static/user_information/{}_recom.txt'.format(user), 'r') as f:
            ans = f.read()
            ans = ans.split('\n')
            ans = [x for x in ans if x != '']
            ans = ans[-10:]
        return list(set(ans))


urls = (
    '/judge', 'judge',
    '/gegu_main', 'gegu_main',
    '/gegu_common', 'gegu_common',
    '/account', 'account',
    '/text', 'text',
    '/pic', 'pic',
    '/register', 'register',
    '/text_res', 'text_res',
    '/text_common', 'text_common',
    '/pic_res', 'pic_res',
    '/recommand', 'recommand'
)

render = web.template.render \
    ('templates/', cache=False,
     builtins={'into_list': into_list, 'into_list_2': into_list_2,
               'print': print, 'open': open, 'int': int, 'floor': math.floor,
               'range': range, 'len': len, 'type': type, 'float': float,
               'random': random.random, 'str': str, 'log': math.log,
               'get_his': get_his, 'search_2': search_3.searchResults,
               'search_1': search_0.search, 'get_hot': get_hot, 'get_url': get_url,
               'match': image_by_image.main, 'add_recom':add_recom,'get_recom':get_recom})


class gegu_main:
    def GET(self):
        vm_env.attachCurrentThread()
        user = web.cookies().get('name')
        user_data = web.input()
        text = user_data.keyword
        index = -1
        with open('static/user_information/{}.txt'.format(user), 'a') as f:
            f.write(text + '\n')
        with open('static/Acodes_names.csv', 'r') as f:
            temp = f.read()
            arr = temp.split('\n')
            arr = [x.split(' ') for x in arr]
            for i in range(len(arr) - 1):
                if arr[i][0] == text or arr[i][1] == text:
                    index = i
                    break
        if index >= 0:
            return render.gegu(index, user, get_star(index))
        else:
            return render.text_res(text, user, -1, 0, 0)


class gegu_common:
    def GET(self):
        vm_env.attachCurrentThread()
        user = web.cookies().get('name')
        user_data = web.input()
        index = int(user_data.index)
        if index < 0:
            text = get_his(user)[-1]
            return render.text_res(text, user, 0, 0, 0)
        return render.gegu(index, user, get_star(index))


class text:
    def GET(self):
        return render.index_text()


class pic:
    def GET(self):
        return render.index_pic()


class account:
    def GET(self):
        user = web.cookies().get('name')
        user_data = web.input()
        index = user_data.index
        return render.accounts(index, user)


class register:
    def GET(self):
        user_data = web.input()
        name = user_data.name
        web.setcookie('name', name, None)
        return render.index_text()


class text_res:
    def GET(self):
        vm_env.attachCurrentThread()
        user = web.cookies().get('name')
        user_data = web.input()
        text = user_data.keyword
        return render.text_res(text, user, 0, 0, 0)


class text_common:
    def GET(self):
        vm_env.attachCurrentThread()
        user = web.cookies().get('name')
        user_data = web.input()
        index = int(user_data.index)
        if index < 0:
            text = get_his(user)[-1]
            return render.text_res(text, user, 0, 0, 0)
        with open('static/Acodes_names.csv', 'r') as f:
            temp = f.read()
            arr = temp.split('\n')
            arr = [x.split(' ') for x in arr]
            name = arr[index][1]
        with open('static/stars.csv', 'r') as f:
            temp = f.read()
            arr = temp.split('\n')
            arr = [x.split(' ') for x in arr]
            num = arr[index][1]
        return render.text_res(name, user, index, 1, num)


class pic_res:
    def POST(self):
        user = web.cookies().get('name')
        x = web.input(myfile={})
        if 'myfile' in x:
            filepath = x.myfile.filename.replace('\\', '/')  # 客户端为windows时注意
            filename = filepath.split('/')[-1]  # 获取文件名
            ext = filename.split('.', 1)[1]  # 获取后缀
            if ext == 'jpg':  # 判断文件后缀名
                filedir = 'static/upload'  # 要上传的路径
                now = datetime.datetime.now()
                t = "%d%d%d" % (now.hour, now.minute, now.second)  # 以时间作为文件名
                filename = t + '.' + ext
                fout = open(filedir + '/' + filename, 'wb')
                fout.write(x.myfile.file.read())
                fout.close()
                message = u'OK！'
                error = False
            else:
                message = u'请上传jpg格式的文件！'
                error = True
                return render.index_pic()
        return render.res_pic(user, filedir + '/' + filename)


class recommand:
    def GET(self):
        user = web.cookies().get('name')
        user_data = web.input()
        index = user_data.index
        return render.recommand(index, user)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
