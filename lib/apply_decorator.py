def apply_decorator(func):
    
    def decorator_func():
        print("Decorator Applied")
        func()  
        print("Main function called")
    
    return decorator_func  


def func():
    print("I am the function")


decorated_func = apply_decorator(func)


decorated_func()
