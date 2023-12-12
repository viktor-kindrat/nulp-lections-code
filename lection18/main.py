# a = 1
# b = 0
# res = None

# try:
#     res = a / b
# except ZeroDivisionError as ex:
#     print(f"Exception caught: {type(ex)}, ex")

# print(res)

# ex = ValueError("My exception")

# raise ex

# name = input("name: ")

# if len(name) < 5:
#     raise ValueError("Name should be more than 4 symbols")
#     print(f"Hello {name}")

# print("end of code")


# lst = [1, 2, 3, 4, 5, 6, 7]

# try:
#     while True:
#         print(lst.pop())
# except IndexError:
#     print("List is empty")
#     print(lst)


lst = (1, 2, 3, 4, 5, 6, 7)

try:
    while True:
        print(lst.pop())
except IndexError:
    print("List is empty")
    print(lst)
except Exception:
    print("Unknown exception")
    
try:
    1 / 0
except Exception as ex:
    print(f"exception occur: {ex}")
    # raise

try:
    # The line `raise ValueError("some text")` is raising a `ValueError` exception with the message
    # "some text". This means that an exception is intentionally being raised at that point in the
    # code.
    raise ValueError("some text")
except Exception as ex:
    # The line `print(f"handled ex {ex}")` is printing the message "handled ex" followed by the value
    # of the exception `ex`. It is used to display the exception that was caught and handled in the
    # `except` block.
    print(f"handled ex {ex}")
# The `finally` block is used to specify a block of code that will be executed regardless of whether
# an exception is raised or not. In this case, the code `print("ok")` will always be executed, whether
# an exception is caught or not. It is commonly used to perform cleanup operations or to ensure that
# certain code is always executed, such as closing files or releasing resources.
finally:
    print("ok")
    

    
# The `MyException` class is a custom exception that takes in an exception name and value and provides
# a string representation of the exception.
class MyException(Exception):
    def __init__(self, ex_name, ex_value):
        self.ex_name = ex_name
        self.ex_value = ex_value
    
    def __str__(self):
        return f"MyException({self.ex_name}, {self.ex_value})"

print(MyException("vdfdbfgb", "dvdfv"))

class MyExceptionA(Exception):
    pass

for num in range(4):
    print(str(num).center(100, "-"))
    try:
        if num == 0:
            raise MyExceptionA("Number equal 0")
        if num in (1, 2):
            raise MyException("wrong number", "wrongNumber")
    except MyExceptionA as ex:
        print(ex)
    except MyException as ex:
        print(ex)