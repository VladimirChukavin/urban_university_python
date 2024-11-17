# Доступ к свойствам родителя. Переопределение свойств

class Human:
    head = True
    _legs = True
    __arms = True

    def say_hello(self):
        print('Hello')

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)


class Student(Human):
    __arms = False
    # def about(self):
    #     print('I am student.')


class Teacher(Human):
    pass


human = Human()
human.about()

student = Student()
student.about()

print(dir(human))
print(dir(student))
print(student._Human__arms)
print(student._Student__arms)