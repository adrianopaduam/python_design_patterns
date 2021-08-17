import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} took {int(end - start) * 1000}ms')
        return result
    return wrapper


@time_it  # this is the decorator in python
def some_op():
    print('Starting the operation')
    time.sleep(1)
    print('We are done')
    return 123


if __name__ == '__main__':
    print(some_op())

    # This is the same as putting the decorator
    # print(time_it(some_op)())
