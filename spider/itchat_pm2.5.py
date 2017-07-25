# coding=utf-8
# itchat.send无法发送汉字消息？连汉字符都不行!
# 只能ASCII码的字符能发送成功
import urllib2
from time import ctime

import urllib2
from bs4 import BeautifulSoup
import itchat


def getPM25(cityname):
    site = 'http://www.pm25.com/' + cityname + '.html'
    page = urllib2.urlopen(site)
    html = page.read()
    soup = BeautifulSoup(html.decode("utf-8"), "html.parser")
    city = soup.find(class_='bi_loaction_city')  # 城市名称
    aqi = soup.find("a", {"class", "bi_aqiarea_num"})  # AQI指数
    quality = soup.select(".bi_aqiarea_right span")  # 空气质量等级
    result = soup.find("div", class_='bi_aqiarea_bottom')  # 空气质量描述
    output = city.text + u'AQI指数：' + aqi.text + u'\n空气质量：' + quality[0].text + result.text
    print(output)
    print('*' * 20 + ctime() + '*' * 20)
    return output


itchat.auto_login(hotReload=True)
itchat.send("Begin getPM25,please edit and send city's pinyin to get data!If pinyin error,return beijing's data!", toUserName='filehelper')


@itchat.msg_register(itchat.content.TEXT)
def getcity(msg):
    if msg['ToUserName'] != 'filehelper': return
    print(msg['Text'])
    cityname = msg['Text']
    result = getPM25(cityname)
    itchat.send(result, 'filehelper')


if __name__ == '__main__':
    itchat.run()
