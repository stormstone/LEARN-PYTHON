__author__ = 'storm'
import urllib2

url = "http://www.baidu.com"

print("1")
response1 = urllib2.urlopen(url)
print(response1.getcode())
print(len(response1.read()))