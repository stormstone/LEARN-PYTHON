# 编写第一个Python程序
print('hello world')
file = open('helloworld.txt', 'w')
file.write('hello world')
file.close()

# 字符串
'char1' + 'char2' + 'char3'
'word' * 3
str = 'My name'
str[0]
str[-4]
str[1:4]
str[3:]
str[:3]
str.split(' ')
# 列表
all_in_list = [
    1,
    1.0,
    'a word',
    print(1),
    True,
    [1, 2],
    (1, 2),
    {'key': 'value'}
]
print(all_in_list)

# 列表的增删改查
fruit = ['pineapple', 'pear']
fruit.insert(1, 'grape')
fruit.insert(-1, 'apple')
fruit = [fruit, 'Apple']

# fruit.remove('grape')
fruit.remove(fruit[0])
del fruit[0:2]

# fruit[0] = 'Orange'
fruit[0:0] = ['Orange']
fruit[-1] = ['end apple']

fruit.append('a')
fruit.append([1, 2, 3])
fruit.extend([1, 2, 3])
