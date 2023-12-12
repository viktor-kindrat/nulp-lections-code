def sum_ (a, b):
    return a + b


sum_2 = lambda a, b: a + b  # function will be used only once. is not recommended to use a lot! Function in one

print(sum_(6, 4))
print(sum_2(6, 4))

student_list = [
    ("Veres", 100, "Ir-11"),
    ("Yatsuk", 51, "Ir-12"),
    ("Pavelchak", 76, "Ir-12"),
    ("Student_1", 87, "Ir-14"), 
]

lst = [1, 6, 2, 9, 3]
print(sorted(lst))

print(sorted(student_list, key=lambda std: std[1]))  # Good example of using labmda functions

class Student:
    def __init__(self, name, rating, group):
        self.name = name
        self.rating = rating
        self.group = group
        
    def __repr__(self):
        return f"Student(\"{self.name}\", {self.rating}, \"{self.group}\")"
    
std1 = Student("Veres", 100, "IR-11")
std2 = Student("Yatsuk", 51, "IR-16")
std3 = Student("Pavelchak", 79, "IR-21")

print("TASK 2".center(100, "-"))

std_list = [std1, std2, std3]

print(sorted(std_list, key=lambda std: std.group))


lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

print(list(map(lambda x, y: x * y, lst1, lst2)))  # map function for mapping lists

lst = ["A, B", "C, D"]
print(list(map(lambda el: el.split(", "), lst)))

lst_a = [1, 3, -3, 0, -7, 12]

# to sort lst_a we can use list comprehantion.
print([el for el in lst_a if el >= 0])
# BUT! We can also use filter function
print(list(filter(lambda a: a >= 0, lst_a)))

print(list(filter(None, range(10))))

lst_false = [0, -120, "", "asd", [], True, False, None, 123, 456.789]
print(list(filter(None, lst_false)))

print("Other task".center(100, "-"))
print(list(filter(lambda el: el.rating > 88, std_list)))

from functools import reduce

lst_4 = [3, 6, 10]

print(reduce(lambda x, y: x + y, lst_4))

print(max(std_list, key=lambda el: el.rating))

lst_c = [1, 2, 3]
lst_d = [4, 5, 6]
lst_e = ["a", "b", "c", "e"]

print(list(zip(lst_c, lst_d, lst_e)))  # concatenate by idx 
# ([(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')])

import itertools
print(list(itertools.zip_longest(lst_c, lst_d, lst_e)))  # concatenate by idx by LONGEST WAY 
# [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c'), (None, None, 'e')]

# 2 WAYS TO MAKE A SUM OF TWO ARRAYS BY IDXS
print(list(map(lambda x, y: x + y, lst_c, lst_d)))
print(
    [x + y for x, y in zip(lst_c, lst_d)]
)
new_lst = list(zip(lst_c, lst_d))

print(new_lst)
lst_a_, lst_b_ = zip(*new_lst)

print(lst_a_, lst_b_)

print(all(lst_false))  # Return True if all el is True
print(any(lst_false))  # Return True if any el is True

