list_1 = [[1, 2, 5], [3, 10, 7]]


print("TASK 1:")
for ind, el in enumerate(list_1):
    for ind1, el1 in enumerate(el):
        print(el1)
        print(list_1[ind][ind1])
        print(el[ind1])
        print("-" * 10)

print("\n\n\n\n\n\n\n\nTASK 2:")
list_2 = list(range(20))

for element in list_2:
    if not element % 2:
        print(element)

print("\n\n\n\n\n\n\n\nTASK 3:")
list_3 = ["str_2", 145.25, "str_5", -2566, 10, True]

for element in list_3:
    print(element)
    if element == 10:
        print(f"the index of element is {list_2.index(element)}")
        print("element 10 was find")
        break

print("\n\n\n\n\n\n\n\nTASK 4:")
for element in list_2:
    if element == 10:
        print("skipping value")
        continue  # 10 was skipped
    print(element * 2)


print("\n\n\n\n\n\n\n\nTASK 5:")
for element in list_3:
    if element == 10:
        break
else:
    print("The sequence contains 10")

print("\n\n\n\n\n\n\n\nTASK 6:")
index = 0
list_4 = list(range(20))
while index < 10:
    print(list_4[index])
    index += 1
