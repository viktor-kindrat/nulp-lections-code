def outer():
    x = 5

    def inner():
        y = 10
        print(x)
    return inner


fnc = outer()
print(fnc.__code__.co_freevars)


def power(n):
    def inner(x):
        return x ** n
    return inner


pow_to_2 = power(2)
print(pow_to_2.__code__.co_freevars)
print(pow_to_2.__closure__)
print("\n" * 5)


def outer(a, b):
    sum_ = a + b

    def inner():
        mul_ = a * b
        print(f"summa: {sum_}\nmultiply: {mul_}")

    return inner


fnc_1 = outer(5, 10)
fnc_1()

print(fnc_1.__closure__)
print("\n" * 5)


def executer(func):
    def inner(*args, **kwargs):
        print(args)
        result = func(*args, **kwargs)
        return result
    return inner


def add_(*args):
    return sum(args)


fnc_3 = executer(add_)

print(fnc_3(1, 2, 3))
print(add_(1, 2, 3))

print("\n" * 2)


def say_hi(name):
    return f"Hi {name}!"


greeting = executer(say_hi)
print(greeting("Dan"))


def wrapper(fnc):
    def inner(*args, **kwargs):
        result = fnc(*args, **kwargs)
        print(f"\nThe fnc {fnc.__name__} and the result is {result}")
        return result

    return inner


add_wrapper = wrapper(add_)
say_hi_wrapper = wrapper(say_hi)

add_wrapper(1, 5, 6)

add_ = wrapper(add_)
add_(2, 5)


@wrapper  # The same that "mul = wrapper(mul)"
def mul(a, b):
    return a * b


mul(4, 10)

from functools import wraps


def fnc_calls(fnc):
    i = 0

    @wraps
    def inner(*args, **kwargs):
        nonlocal i

        result = fnc(*args, **kwargs)
        i += 1

        print(f"function {fnc.__name__} called {i} times")
        return result

    return inner


@fnc_calls
def div(a, b):
    """
    :param a: Int
    :param b: Int
    :return: Float
    """
    return a / b


div(2, 4)
div(2, 4)
div(2, 4)
div(2, 4)
div(2, 4)
div(2, 4)
div(2, 4)

print(div.__name__)
