# -*- coding: utf-8 -*-
import url_manager
import html_download
import html_outputer
import html_parser

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)

        print(len(self.urls.new_urls))

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_url)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break

                count += 1
            except:
                print('craw failed')

        self.outputer.out_put_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/link?url=fAG5_7ViPkQVab4dcyJrOsrIfxFm9SDSVnUkNMIyvqkoVjRPw0XqelYLyVyavrf8Ph8KRQNT97nEDXtpSAeIt_'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)