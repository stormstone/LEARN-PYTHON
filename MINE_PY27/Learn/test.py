#coding=utf-8
from flask_script import Manager
__author__ = 'storm'
import random
canteens = [u'黑店', u'学苑0',u'学苑1',u'学苑2', u'学士1',u'学士2', u'学士3', u'18公寓']
after6 = [0,4,7]

def main():
    print "haohao"
    if raw_input() != '6':
        print canteens[random.randint(0, len(canteens)-1)]
    else :
        print canteens[after6[random.randint(0, len(after6)-1)]]

if __name__ == '__main__':
    main()