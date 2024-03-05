# Decorator function
def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

# Function decorated with the decorator


@my_decorator
def say_hello():
    print("Hello, world!")


# Calling the decorated function
say_hello()
