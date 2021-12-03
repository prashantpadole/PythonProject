class decorator_class(object):

    def __init__(self,original_func):
        self.original_func=original_func

    def __call__(self, *args, **kwargs):
        print("call method executed this before actual {} method".format(self.original_func.__name__))
        return self.original_func(*args,**kwargs)

@decorator_class
def display():
    print("Display function ran")
@decorator_class
def display_info(name,age):
    print("display infor ran with args {} and {} ".format(name,age))

display()
display_info("Lux",30)


'''
__init method is to tie original function to the class instance
__call__ method is equivalent to wrapper method in function decorator

'''