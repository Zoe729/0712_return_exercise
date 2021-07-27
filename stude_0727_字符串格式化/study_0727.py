

"""
0727  字符串格式化
"""

"""
# 我是 Zoe，今年 18 歲
"""

name = 'Zoe'
age = 18

name1 = 'Water'
age1 = 25

# ------------------------------------------------------------------------


# 最笨方法
newName_1 = '我是' + name + '，' + '今年' + str(age) + '歲'
print (newName_1)


# python2 用法， %s、%d 各有代表的意思，%s 為 str
newName_2 = '我是 %s，今年 %d 歲' % ( name , age )
print (newName_2)


# python3 用法，不用將 int 轉換 str
newName_3 = '我是 {}，今年 {} 歲'.format( name , age )
print (newName_3)


# python3 用法，不用將 int 轉換 str，且不受位置拘束
newName_4 = '我是 {name}，今年 {age} 歲'.format( name = 'cute Zoe' , age = '20' )
print (newName_4)


# python3.6後 用法 ( 直接帶入外面設定好的數值 )
newName_5 = f'我是 {name}，今年 {age} 歲'
print (newName_5)


newName_6 = f'我是 {name1}，今年 {age1} 歲'
print (newName_6)



# split()、join()-----------------------------------------------------------------

a = ' Zoe is so cute'
print ( a.split() )
# 印出 ['Zoe', 'is', 'so', 'cute']
# split默认不传如参数，就会按照空格分割

b = ' Zoe = is = so = cute'
print ( b.split('=') )
# 印出 [' Zoe ', ' is ', ' so ', ' cute']
# 去除 = 


x = 'hello world'
x.split(' ') 
# split() - str.split(str="", num=string.count(str)).
# (參數) str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# (參數) num -- 分割次数。默认为 -1, 即分隔所有。
# 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串


print (x.split(' '))
# 印出 ['hello', 'world']


print(' '.join(['hello', 'world']))  
# 印出 hello world
# join()方法 - str.join(sequence)，sequence -- 要连接的元素序列
# 返回通过指定字符连接序列中元素后生成的新字符串。



p = '123456'
print(p.split('234'))
# ['1', '56']



