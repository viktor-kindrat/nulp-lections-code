list_1 = [element ** 2 for element in range(20) if not element % 2]  # List comprehension

print("List 1: ", list_1)

list_2 = [(element ** 2 if element % 2 else False) for element in range(20)]  # List comprehension

print("List 2: ", list_2)

list_3 = [
    element ** 2
    for element in range(20)
    if not element % 2
]  # List comprehension not flat

print("List 3: ", list_3)

dict_1 = {
    f"{idx}": element ** 2
    for idx, element in enumerate(range(20))
    if not element % 2
}  # Dictionary comprehension

print(dict_1)


set_2 = {
    f"{idx}"
    for idx, element in enumerate(range(20))
    if not element % 2
}  # Set comprehension

print(set_2)