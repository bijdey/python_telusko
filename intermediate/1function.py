

## in this function we are hardcoding the values
def add():
    a=2
    b=1
    c= a+b
    print(c)


##calling the add function(the hardcorded function)
add() ##this is the hardcorded function


def addition(a,b):
    print(a+b)

##calling the addition function (dynamic function)
addition(3,5)



def sum(a, b):
    return a+b
##printing the function like this also, here nothing will be printed if we use #sum(3,6)
print(sum(9,8)) 



## an important concept, how none gets printed,

def addno(x,y):
    a= x
    b= y
    c=a+b
    print(c)

result= addno(5,7) ## as result is not storing,
##it will store when we use return not when we use print, see below for more
print('result is', result) ## result is None



## so to get value printed as we are storing we need to use the return

def addnum(x,y):
    a= x
    b= y
    c=a+b
    return c 

result= addnum(5,7) ## as result is not storing,
##it will store when we use return not when we use print, see below for more
print('result is', result) ## result is 12



