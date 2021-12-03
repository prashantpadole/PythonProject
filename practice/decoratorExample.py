import time

from functools import wraps
def my_logging(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__),level=logging.INFO)
    @wraps(original_function)
    def wrapper_function(*args,**kargs):
        logging.info('Ran with arg {} and kargs {} '.format(args,kargs))
        return original_function(*args,**kargs)
    return wrapper_function

def my_time(original_function):
    import time
    @wraps(original_function)
    def wrapper_function(*args,**kargs):
        t1=time.time()
        result= original_function(*args,**kargs)
        t2=time.time()-t1
        print("{} ran in {} sec ".format(original_function.__name__,t2))
        return result

    return wrapper_function
@my_logging
@my_time
def display():
    time.sleep(3)
    print("display function is executed ")

@my_logging
@my_time
def display_info(name,age):
    time.sleep(5)
    print("display info function is executed with arg {} and krgs {}".format(name,age))

display_info("Johnson",27)

display()