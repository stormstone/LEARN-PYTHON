# -*- coding: utf-8 -*-
# @Time    : 2017-10-11 20:05
# @Author  : Storm
# @Site    : 
# @File    : day03.py

import re

lyr = 'The night begin to shine, The night begin to shine.'
words = lyr.split()
li = [re.sub('[,.]', '', word) for word in words]
print(li)
print(li.count('shine'))

print('--------------------------------')

'''
练习4:自定义函数,将指定文本中的敏感词过滤后写入桌面指定位置的txt文档中。
1)自定义函数Repalce,将某些敏感词(比如“暴力”)替换成“和平”；
2)自定义函数texcreat(name,text),将text写入“name.txt”文件中；
3)自定义函数final_t将敏感词过滤后的文本写入指定txt文档中。
'''

str = '暴力世界'


def Replace(word, old_word='暴力', new_word='和平'):
    return word.replace(old_word, new_word)


def texcreat(name, text):
    path_fu = name + '.txt'
    f = open(path_fu, 'w')
    f.write(text)
    f.close()


def final_t(name, msg):
    text = Replace(msg)
    texcreat(name, text)


print(Replace(str))
print(Replace(str, '世界', '核平'))
print(Replace(word=str, new_word='核平', old_word='世界'))

texcreat('test', 'sgf')

final_t('storm', '暴力世界\n暴力世界\n暴力世界\n暴力世界\n暴力世界\n暴力世界\n暴力世界\n暴力世界\n')

print('--------------------------------')

'''
练习5:掷骰子(3颗)猜大小游戏。
1)自定义函数roll_dice,生成3个骰子的点数列表；
2)自定义函数roll_result(),返回3颗骰子点数和的大小(以11为界)；
3)自定义函数start_game(),要求从键盘输入:Big或者Small,并返回猜大小的结果。
'''
import random


def roll_dice(nu=3):
    points = []
    while nu > 0:
        points.append(random.randrange(1, 7))
        nu -= 1
    return points


def roll_result(total):
    if total >= 11:
        return 'Big'
    else:
        return 'Small'


def start_game():
    print('<<< START GAME >>>')
    your_choices = input('Big or Small: ')
    choices = ['Big', 'Small']
    if your_choices in choices:
        points = roll_dice()
        total = sum(points)
        if your_choices == roll_result(total):
            print('The points are ', points, ' you win!')
        else:
            print('The points are ', points, ' you !')
    else:
        print('Invalid input')


res = start_game()
print(res)
