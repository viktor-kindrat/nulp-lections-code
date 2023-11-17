class Car:
    @staticmethod  # This is bad! Not use it
    def run_car(start):
        print("Car is riding...")
        
        
Car.run_car("dfvsdfvsd")

newCar = Car()
newCar.run_car("dfvdfv")

print("TASK 2".center(100, "-"))

class Aircraft:
    def __init__(self, thrust, lift, max_speed):
        self.thrust = thrust
        self.lift = lift
        self.max_speed = max_speed
        
    def show_technical_spec(self):
        print(f"Thrust {self.thrust}")
        print(f"Lift {self.lift}")
        print(f"Max speed {self.max_speed} km/h")
        
    def print_data(self):
        self.show_technical_spec()

plain = Aircraft(5000, 2500, 1500)

plain.show_technical_spec()

class Helicopter(Aircraft):
    def __init__(self, num_rotors, thrust=100000, lift=500, max_speed=1000):
        super().__init__(thrust, lift, max_speed)
        self.num_rotors = num_rotors
        
    def show_technical_spec(self):
        super().show_technical_spec()
        print(f"Number of rotors {self.num_rotors}")
        
hel = Helicopter(0, 5000, 5000, 500000)

print(hel.__dict__)
print("TASK 3".center(100, "-"))
hel.show_technical_spec()
print("TASK 4".center(100, "-"))
hel.print_data()

print("TASK WITH WORKER".center(100, "-"))

class Worker:
    def __init__(self, name, adress, salary_per_hour):
        self.name = name
        self.adress = adress
        self.salary_per_hour = salary_per_hour
        
    def calculate_salary(self, hours): 
        return self.salary_per_hour * hours
    
    
class Manager(Worker):
    def __init__(self, name, adress, salary_per_hour, bonus_per_hour):
        super().__init__(name, adress, salary_per_hour)
        self.bonus_per_hour = bonus_per_hour
        self.full_salary = self.bonus_per_hour + self.salary_per_hour
        
    def count_bonus(self, hours):
        return self.bonus_per_hour * hours
    
    def calculate_salary(self, hours):
        return self.full_salary * hours
    
manager1 = Manager("petro", "Lviv", 10, 2)
print(manager1.calculate_salary(40))
    
print("TASK WITH WORKER. Security".center(100, "-"))
    
class Security(Worker):
    pass

security1 = Security("Oleg", "Lviv", 12)
print(security1.calculate_salary(40))

print("TASK 4".center(100, "-"))

class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")

class C(A):
    def method(self):
        print("C.method")

class D(B, C):
    pass
    
print(D.__mro__)

newD = D()
newD.method()

print("Abstract class".center(100, "-"))
from abc import ABC, abstractmethod

def Shape(ABC):  # ABSTARCT CLASS
    @abstractmethod
    def get_area():
        pass
    
    @abstractmethod
    def get_perimetr():
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def get_perimetr(self):
        return self.radius * 2 * pi
    
    def get_area(self):
        return pi * self.radius ** 2 
