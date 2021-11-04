def ExceptionTest(x):
    if x>100:
        print("number is greatr than 100")
        y = x/10
        print(y," is final result")
    else:
        print("divide number by 0")
        y=x/0
        print(y,"final result")

count=0
try:
    Exception(105)
    ExceptionTest(99)
    ExceptionTest(98)
except ZeroDivisionError:
    print("Zero division error occured")

finally:
    count=count+1
    print("executed {} time".format(count))


