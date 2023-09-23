# print(list(range(5, 10, 2)))  # [5, 7, 9] range(start, stop, step)

list_1 = [1, 2, 5, 10, "vgbfgbfg"]

# for i in range(5, 10):
#     print(i)
# print("done")

# for index in range(len(list_1)):
#     print(index, list_1[index])
#
# for enum in enumerate(list_1, start=0):
#     index, value = enum
#     print(index, value)

for index, value in enumerate(list_1, start=0):
    print(index, value)
