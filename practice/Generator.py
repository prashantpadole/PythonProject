

def square_num(num):
    for i in num:
        yield i*i



my_result=square_num([1,2,3,4,5])
print(list(my_result))

for i in my_result:
    print(i)


#### List comprehension

result=[x*x for x in [1,2,3,4,5]]
print(result) ## list comprehension

result=(x*x  for x in [1,2,3,4,5])
print(result) ## generator