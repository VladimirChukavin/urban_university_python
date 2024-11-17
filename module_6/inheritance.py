# Цели и задачи. Зачем нужно наследование

class Human:
    head = True

    # def __init__(self):
    #     self.about()
    def say_hello(self):
        print('Hello')


class Student(Human):
    head = False

    def about(self):
        print('I am student.')

    # def say_hello(self):
    #     print('Hello')


class Teacher(Human):
    pass
    # def say_hello(self):
    #     print('Hello')


# human = Human()
student = Student()
# print(human.head)
student.about()
print(student.head)
# human.about() # error
teacher = Teacher()
teacher.say_hello()
student.say_hello()