import web
#import SearchFiles_web
#import SearchFiles_img


urls = (
    '/gegu', 'gegu'
)

render = web.template.render('templates/', cache=False)  # your templates


class index_web:
    def GET(self):
        return render.index_web()


class s_web:
    def GET(self):
        render = web.template.render('templates', builtins={})
        #{'search': SearchFiles_web.search, 'len': len})
        user_data = web.input()
        return render.res_web(user_data.keyword)

class index_img:
    def GET(self):
        return render.index_img()


class s_img:
    def GET(self):
        vm_env.attachCurrentThread()
        render = web.template.render('templates', builtins={})
        #{'search': SearchFiles_img.search, 'len': len})
        user_data = web.input()
        return render.res_img(user_data.keyword)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
