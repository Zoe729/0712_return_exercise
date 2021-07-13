
#-----------------------------

def test () :
    return 'Zoe'

print (test()) # Zoe

#-----------------------------

a = 1
b = 2

def test ( a , b ) :
    c = a + b
    return c

print (test(a , b)) # 3

#-----------------------------

a = 'apple'
b = 'banana'

def test ( a , b ) :
    return a

print (test(a , b)) # apple

#-----------------------------

def fortest ( a ) :
    for b in range( 1 , 6 ) : 
        c = a * b  
    return c

d = fortest ( 5 )
print( d ) # 25 ，return 只會回傳一個值

#-----------------------------

def sad ( x , y ):
    if x == y:
        return x , y
    else:
        return 'so sad'

print (sad ( 2 , 5 )) #so sad
print (sad ( 4 , 4 )) #(4, 4)

#-----------------------------

def test ( a , b ): 
    c = a * b
    return c


for d in range ( 1 , 4 ):  
    e = test ( 1+d , 10 ) 
    print (e) # 1+1*10=20、1+2*10=30、1+3*10=40

#-----------------------------

