class Arm:
    def __init__(self):
        self.position = 0

    def move_up(self):
        print("Moving up")

    def move_down(self):
        print("Moving down")

    def weld(self):
        print("Welding...")


class Body:
    def rotate_left(self):
        print("rotating left")

    def rotate_right(self):
        print("rotating right")


class Robot:  # "Composing"
    def __init__(self):
        self.body = Body()
        self.arm = Arm()

    def rotate_left(self):
        self.body.rotate_left()

    def rotate_right(self):
        self.body.rotate_right()

    def move_up(self):
        self.arm.move_up()

    def move_down(self):
        self.arm.move_down()

    def action(self):
        self.arm.weld()


class Singletone:
    _instanse = None

    def __new__(cls, *args, **kwargs):
        if cls._instanse is None:
            print("created successfully")
            cls._instanse = super().__new__(cls)
        else:
            print("already exist")
        return cls._instanse

ins = Singletone()

ins_2 = Singletone()
ins_3 = Singletone()
