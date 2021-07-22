


# ------------------------------------------

list_1 = [ 'slot','casino','nember']
list_2 = [ 'one','two','three']

print ( 'list_1[0] :' + list_1[0] )
print ( 'list_2[0] :' + list_2[0] )


# ------------------------------------------

list1 = []
list1.append('1')
list1.append('2')
list1.append('3')
print ( list1 )


# ------------------------------------------

list2 = []
for a in range(1,6):
    list2.append(a)
print ( list2 )
print ( list2[1] )

del list2[1]
print ( list2 )


# ------------------------------------------

list3 = [ '1','2','3','4','5']
list4 = [ '2','4','6','8','2','2']


list3.append('6')
del list3[4]

# print ( list3 )
# print ( len(list3) )

print (list4.count('2'))  # list4.count() -- 計算 2 在 list4 中出現的次數

list3.extend(list4) # list3.extend(list4) -- 合併兩個列表內容
print (list3)

print(list3.index('4'))  # list3.index -- 找到 List3 中，4 的位置

list3.insert( 1,'0') # list3.insert( 1,'0')，在 list3 中的 第一個位置，插入 0
print (list3)

list3.reverse() # list3.reverse()，反向顯示 list3 中的內容
print(list3)


# ------------------------------------------

list5 = []
list6 = [ '1','2','3','4','5']

def show ():
    for a in range(len(list6)):
        list5.append('happy'+ str(a))
    
show ()
print( list5 )


# ------------------------------------------
