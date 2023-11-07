class Vers:
    # ... code from previous lection

    def __eq__(self, other):  # "==" function
        if not isinstance(other, Vers):  # checking instance of object
            raise TypeError("Wrong object type")

        return (
            self.major == other.major
            and self.minor == other.minor
            and self.patch == other.patch
        )
        return result

    # if we redefine __eq__ we MUST to redefine __hash__

    def __hash__(self):
        return hash(
            (self.__major, self.__minor, self.__patch)
        )  # method hash return hash sum of given list or tuple (tuple is better. has less memory capacity)

    def __ne__(self, other):  # stands from "not equal"
        return not self == other

    def __lt__(self, other):  # self < other
        if not isinstance(other, Vers):
            raise TypeError("Wrong object type")
        
        if self.__major != other.major:
            result = self.__major < other.major
        elif self.__minor != other.minor:
            result = self.__minor < other.minor
        else:
            result = self.__patch < other.patch
            
        return result
    
    def __ge__(self, other):  # self >= other
        return not self < other
    
    def __gt__(self, other): # self > other
        if not isinstance(other, Vers):
            raise TypeError("Wrong object type")
        
        if self.__major != other.major:
            result = self.__major > other.major
        elif self.__minor != other.minor:
            result = self.__minor > other.minor
        else:
            result = self.__patch > other.patch
            
        return result
    
    def __le__(self, other):  # self <= other
        return not self > other
    

class X:
    def __init__(self, num):
        self.num = num
        
    def __str__(self):
        return f"x = {num}"
    
    def __add__(self, other): 
        return X(self.num + other.num)
    
    def __radd__(self, other):  #right side add
        return X(self.num + other.num)

class Y:
    def __init__(self, num):
        self.num = num
    
    def __str__(self):
        return f"y = {num}"



