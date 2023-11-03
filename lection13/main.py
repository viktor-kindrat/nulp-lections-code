# functools

class FirstClass:
    pass


class Student:
    rating = 2
    group = "IR11111"


print(Student.rating)

print("\n" * 5)

first_student = Student()

print(first_student.rating)
first_student.rating = "new_value"
print(first_student.rating)

second_student = Student()

print(type(second_student) is Student)


class Student:
    rating = 0

    def set_rateing(self, new_value):
        self.rating = new_value


stdnt = Student()
stdnt.set_rateing(80)
print(stdnt.rating, Student.rating)

stdnt_2 = Student()
stdnt_2.set_rateing(80)
print(stdnt_2.rating, Student.rating)

print("\n" * 10)


class Student:
    def __init__(self, surname, name, rating):
        """
        Initialize class
        """
        self._surname = surname  # PROTECTED (can be reached outside)
        self.__name = name  # PRIVATE (can not be reached outside)
        self.rating = rating

    @property
    def surname(self):
        return self._surname


    @property.setter
    def surname(self, new_surname):
        self._surname = new_surname

    # THE SAME AS UPPER
    #
    # def set_surname(self, new_value):
    #     self._surname = new_value
    #
    # def get_surname(self):
    #     return self._surname
