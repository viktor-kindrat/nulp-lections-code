list_1 = [1, 2, 5, 10]

print(" > ".join(str(x) for x in list_1))

string = 'gfbhnh'

print(".".join(string))

a = 123
b = 321

a, b = b, a # unpacking (use tuples for destructuration)

# a, b, c, d, e, j = list_1 # exception
# print(a, b, c, d, e, j)

f_el, *_, l_el = list_1 # unpacking (*_)

print(_)

print(globals())

