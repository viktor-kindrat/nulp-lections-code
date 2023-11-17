from abc import ABC, abstractmethod


class TestABC(ABC):
    @abstractmethod
    def method_1(self):
        """
        Method number 1
        :return:
        """
        print("Hello from abstract method")

    def method_2(self):
        print("Hi from method 2")


class TestClass(TestABC):
    """
    Test class
    """

    def method_1(self):
        print(f"hello from method {type(self).__name__}")


class TemplateMethod(ABC):
    def template_method(self):
        self.find_file()  # find file
        self.open_file()  # open file
        self.read_data()  # read file
        self.convert_file()  # convert to text
        self.print_save()  # print
        self.send_data()  # Send data (the same for all instances)

    @abstractmethod
    def find_file(self):
        pass

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def convert_file(self):
        pass

    @abstractmethod
    def print_save(self):
        pass

    def send_data(self):
        print("...Sending")


class JsonConvertor(TemplateMethod):
    """
    This class converts JSON to text
    """

    def open_file(self):
        print("Opening file")

    def read_data(self):
        print("Reading")

    def convert_file(self):
        print("Converting JSON to Text")

    def find_file(self):
        print("Searching")

    def print_save(self):
        print("Hello world")


class XmlConvertor(TemplateMethod):
    """
    This class converts JSON to text
    """

    def open_file(self):
        print("Opening file")

    def read_data(self):
        print("Reading")

    def convert_file(self):
        print("Converting XML to Text")

    def find_file(self):
        print("Searching")

    def print_save(self):
        print("Hello from XML")


jsn = JsonConvertor()
jsn.template_method()

