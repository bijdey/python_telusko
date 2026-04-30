
x= 10

print(type(x)) #<class 'int'>

pi= 3.14

print(type(pi)) #<class 'float'>

c= 6+8j #for the complex number, note that for complex only 'j' can be used

print(type(c)) #<class 'complex'>



###

n= 3
m= 9
d=complex(n,m)
print(d) #(3+9j)

##
pie= 3.14
k=int(pie)
print(k, type(k), sep=", ")  # 3, <class 'int'>


numi= 5
numd=float(numi)
print(numi, numd, type(numi),  type(numd),  sep=", ")  # 5, 5.0, <class 'int'>, <class 'float'>


##
no= 5
fno=float(no)
print(fno, type(fno), sep=', ')



#####
##booliean
a=7
b=2
greater= b>a
print(greater, type(greater)) # False <class 'bool'>


####
val=True
print(val) #True
k= int(val)
print(k) #1


##none

# Printing None directly
print(None)  # None

# Assigning None to a variable and printing
x = None
print(x)  # None

# Checking type
print(type(None))  # <class 'NoneType'>

# In different contexts   
result = None
print(f"The result is: {result}")  # The result is: None


####
## Some more about the list
l=[1, 3, 5, 534]
print(type(l)) #<class 'list'>

##tupple
t=(34,54,243) ## or t= 34, 54, 243
print(type(t)) ## <class 'tuple'>

##set
s={4, 56, 6}
print(type(s)) ##<class 'set'>


##
##range
r=range(10) ##note that the last one is not included
print(r, type(r), sep=', ') ##range(0, 10), <class 'range'>


print(list(r)) ## 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(set(r)) ## {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


