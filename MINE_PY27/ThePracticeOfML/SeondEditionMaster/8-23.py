# -*- coding: utf-8 -*-
#code:myhaspl@myhaspl.com
#8-23.py
from fp_growth import find_frequent_itemsets
import csv
myminsup=200#设定最小支持度
if __name__ == '__main__':
    f = open("sales.csv")
    try:
        for itemset, support in find_frequent_itemsets(csv.reader(f), myminsup, True):         
            print '{' + ','.join(itemset) + '} ' + str(support)
    finally:
        f.close()