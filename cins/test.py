__author__ = 'storm'

import getopt
import requests
import sys
import os
def main():
    option, argv = getopt.getopt(sys.argv[1:], "d:")
    print(len(sys.argv))
    if len(sys.argv) <= 2:
        print('[-] python 1', sys.argv[0], '-d')
        sys.exit(0)
    for i, j in option:
        if i == '-d':
           lfile = j
           break
        print('[-] python 2', sys.argv[0], '-d')
        sys.exit(0)
    url = "http://www.baidu.com"
    r = requests.get(url)
    html = r.text
    html = html.encode('ISO-8859-1')
    try:
        file = open(lfile, 'w')
        file.writelines(html)
        print('success')
        file.close()
    except:
         print("Error")

if __name__ == '__main__':
    main()

