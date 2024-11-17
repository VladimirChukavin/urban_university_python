# Множественное наследование. Метод Super

class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()

    def info(self):
        print(f'Hello, my name is {self.name}')


class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} in group {self.group}')


class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()


# human = Human('John')
# print(human.name)

student = Student('Jany', 'Urban', 'Python 1')
print(student.name, student.place)
print(student.group)
student.about()

# print(Student.__mro__)
# print(Student.mro())
# print(Human.mro())
