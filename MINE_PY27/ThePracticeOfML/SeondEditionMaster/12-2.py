#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#12-2.py

import jieba
seg_list = jieba.cut("2010年底部队友谊篮球赛结束", cut_all=False)
print "Default Mode:", "/ ".join(seg_list) # 默认模式
