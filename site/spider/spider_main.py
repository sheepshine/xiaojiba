# coding:utf8
from spider import url_manage, html_downloader, html_parser, html_outputer


class SpiderMan(object):
    def __init__(self):
        self.urls = url_manage.UrlManage()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            #try:
            new_url = self.urls.get_new_url()
            print 'cras %d : %s' %(count, new_url)
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parser(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)

            if count == 100:
                break

            count = count + 1
            #except Exception as e:
               # print e

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = SpiderMan()
    obj_spider.craw(root_url)
