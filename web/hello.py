import web
import MySQLdb

from urls import urls
import dbsetting

app = web.application(urls, globals())

render = web.template.render('temp')


class index:
    def GET(self):
        query = web.input()
        return query


class blog:
    def POST(self):
        data = web.input()
        return data

    def GET(self):
        return web.ctx.env


class hello:
    def GET(self, name):
        db = MySQLdb.Connect(
            host=dbsetting.db['host'],
            port=dbsetting.db['port'],
            user=dbsetting.db['user'],
            passwd=dbsetting.db['passwd'],
            db=dbsetting.db['db'],
            charset=dbsetting.db['charset']
        )
        cur = db.cursor()
        sql = 'SELECT * FROM test'
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        db.close()
        return render.hello(res)


class getList:
    def GET(self):
        return str('list')


if __name__ == '__main__':
    app.run()