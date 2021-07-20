

# 累加 * -------------------------------( range )

a = '*'
for b in range (5):
    c = a * b
    print (c)



# 數字總和 ------------------------------( range )

sum = 0
for b in range (1,6):
    sum = sum + b
    print (sum)

''' 
◎ (優先處理+號的運算) 先算後面的 +，再算 =，後面的數字是迴圈的 12345
◎ 得到 總和的 sum 後，第二輪 也是先將 sum 帶到加減的運算中，算出總合的 sum，以此類推
sum += i   ==   sum = sum + I

1 = 0 + 1
3 = 1 + 2
6 = 3 + 3
10 = 6 + 4
15 = 10 + 5

'''


# List 迴圈 ----------------------------( range )

b = ['apple','banana']
for a in (b):
    print(a)



# 用 迴圈 建立 List --------------------( range )

c = []
for a in range (1,4):
    c.append('Zoetest'+str(a))
print (c)
print (c[0])



# 用 迴圈 跑 function return 值 --------------------( range )

def abc ():
    return 'Zoe'
c = 'so cute' + '' + abc()
print(c)

for a in abc():
    print (a)



# 用 迴圈 建立 乘法表  --------------------( range )
# 巢狀迴圈分別有外部迴圈(Outer loop)及內部迴圈(Inner loop)，程式執行的時候，會先從外部迴圈取得第一個元素 ，接著執行內部迴圈(1~9)，直到內部迴圈執行完畢，才會回到外部迴圈取得第二個元素 

for a in range (1,10):
    for b in range(1,10):
        c = a * b
        print( str(a) + '*' + str(b) + '=' + str(c) )


for name in 'zoe':
    for number in range (1,4):
        print (name , number)



# 用  break 終止迴圈   --------------------( range )
# 使用for-loop讀取1到9的整數數列，當迴圈讀取到數字5時，由於整除3，執行了break指令，之後的print()方法沒有執行且中斷迴圈

for a in range(1,10):
    if a % 5 == 0 :
        break
    print(a)



# 用  continue   --------------------( range )
# 使用for-loop讀取1到9的整數數列，當讀取到的數字能夠整除3，之後的print()方法就不會執行，但是迴圈不會中斷，繼續讀取下一個元素，所以執行結果印出沒辦法整除5的數字

for a in range(1,10):
    if a % 5 == 0 :
        continue
    print(a)



# 用 迴圈 跑 字典 --------------------------------

dic = {
    'a' : 'apple',
    'b' : 'banana',
    'c' : 'candy'
}

for key,value in dic.items():
    print (key)
    print (value)
    print (key,value)



# 用 迴圈 跑 巢式字典--------------------------------

dic = {
    'a' : {
        '1' : 'apple',
        '2' : 'ability',
        '3' : 'art'
    },
    'b' : {
        '1' : 'banana',
        '2' : 'but',
        '3' : 'baba'
    }
}

for key,value in dic.items():
    for key1,value1 in value.items():
        print (key1,value1)