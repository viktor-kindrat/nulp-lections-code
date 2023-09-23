# ls = [1, 4, 2, 34, "str1", "str2"]

# print(ls[0])
# print(len(ls)) # list length
# print(ls[len(ls) - 1])
# print(ls[-1])

# ls.append(636)
# print(ls[-1])
# print(len(ls)) # list length


# print(dir(ls))
# print(ls.__doc__)


# nums = [1, 2, 5, -59, 0]
#
# print(nums * 3)

my_list = [1, True, "str", [1.2, 3, 5], [6, 3.2, 2], "vdfvdvdf"]

# print(my_list[3][0])

# print("Before", my_list)
# my_list.extend([1.5, 10])
# print("After", my_list)

print(my_list[2:7]) # Result => ALWAYS NEW OBJECT

print(my_list == my_list[:]) # True
print(my_list is my_list[:]) # False
print(my_list[::-1])
print(my_list.reverse())

