import re


class TestClass:
    def __init__(self):
        pass


test_class = TestClass()

setattr(test_class, "name", "value")

print(getattr(test_class, "name", "none"))
print(getattr(test_class, "name1", "none"))


class Student:
    # def __new__
    def __init__(self, surname, name, rating=51):
        self.__surname = surname
        self.__name = name
        self.__rating = rating
        Student.group = "IR11"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __str__(self):  # What do
        return f"Student surname: {self.__surname}, name: {self.__name}, rating: {self.__rating}"

    def __repr__(self):  # Representation
        return f"Student({self.__surname}, {self.__name}, {self.__rating})"

    def get_full_name(self):
        return f"{self.__surname} {self.__name}"

    def get_mark(self):
        if 88 <= self.__rating <= 100:
            result = "A"
        elif 71 <= self.__rating <= 87:
            result = "B"
        elif 51 <= self.__rating <= 71:
            result = "C"
        else:
            result = "expelled"

        return result

    def set_rating(self, new_rating):
        self.__rating = new_rating

    def __transform_name(self):
        return self.__surname.upper()


new_stud = Student("vfdvg", "dgbdgbdg", 81)

print(new_stud.name)
print(new_stud)

print(repr(new_stud))

print(new_stud.get_mark())


class Number:
    @staticmethod  # If there is no need to use "self"
    def add_two_numbers(num_1, num_2):
        return num_1 + num_2


print(Number.add_two_numbers(5, 10))

num_ex = Number()
print(num_ex.add_two_numbers(5, 10))

# major.minor.patch.build

class Version:
    # regex101
    SEARCH_PATTERN = r"(\d+)[._]"

    def __init__(self, version_str):
        self.__version_str = version_str
        self.__major = None
        self.__minor = None
        self.__patch = None
        self.__parse()

    def __parse(self):
        result = re.search(Version.SEARCH_PATTERN, self.__version_str)
        if result is not None:
            self.__major = int(result.group(1))
            self.__minor = int(result.group(2))
            self.__patch = int(result.group(3))
        else:
            raise ValueError("Given str doesn't provide valid info")

    def __str__(self):
        return f"Major={self.__major} Minor={self.__minor} Patch={self.__patch}"








