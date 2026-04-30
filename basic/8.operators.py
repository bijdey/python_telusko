

a=2
b=4
print(a+b)
print(a//b, a/b, a%b, sep=', ') #0, 0.5, 2


##some new things

a = 3
a += 2
print(a)  #  5


##assign many variables in one line
x,y= 4,5
print(x,y, sep=', ') # 4, 5


a= 8
print(-a) # note that the value of a is not negative, 
#it is uninary operator here as it is single and here we are printing as talking as -a

a=6
a=-a
print(a) # -6

####

a,b= 4,3

print(a>b) # True
print(a<=b) # FAlse
print(a!= b) #True


###
#####

##logical operator
## in case of 'and' we get always true when both are true, else we get false
## in case of 'or' we get always false when both are false, else we get true

a,b= 4, 5
print(a<10)
print(a<10 and b>1)## True
print(a<30 and b>20) ##False

print(a>3 or b>40) ## True
print(a>40 or b<3) ## False


##not reverses 
result=True
print(not result) #False
