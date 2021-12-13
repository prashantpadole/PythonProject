def decorator_function(original_fun):

    def wrapper_function(*args,**kargs):
        print("Wrapper ran before display function")
        return original_fun(*args,**kargs)

    return wrapper_function



@decorator_function
def display():
    print("This is a Test program for Decorator")

@decorator_function
def display_info(name,age):
    print("{} is running test at the age of {}".format(name,age))

display_info("John",25)
display()

##

