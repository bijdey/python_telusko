#513 note that before this learn the filter first
#suppose i want the double of the even number from the nums list

from functools import reduce #we imported to use the reduce function


nums=[4, 3, 56, 67, 89, 2, 43, 88, 95]
even= list(filter(lambda n: n%2==0, nums))
print('even-', even) #even- [4, 56, 2, 88]

double= list(map(lambda x: x*2 , even))
print('double-', double) #double- [8, 112, 4, 176]


#reduce function
# note that lambda can take two parameter so here total is 8 and num is 112 in first call
# note that here total gets changed when num changes from the list
# in simple words reduce function takes 2 values
sum_it= lambda total, num: total + num
sum=reduce( sum_it  ,double )
print(sum) # 300


# in single line

sum=reduce( lambda total, num: total + num  ,double )
print(sum)



