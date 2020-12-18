import functools

# @mydecorator
# def dosomething():
#     pass


def start_end_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper


@start_end_decorator
def print_name():
    print('Alex')


# print_name = start_end_decorator(print_name)


print_name()


def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper


@start_end_decorator
def add5(x):
    return x + 5


result = add5(10)
print(result)

print(help(add5))
print(add5.__name__)
