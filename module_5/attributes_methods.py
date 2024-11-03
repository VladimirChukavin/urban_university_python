# Атрибуты и методы объекта. Указатель на свой объект в методах

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Hello, my name is {self.name}, my age is {self.age}')

    def life_length(self):
        self.age += 1
        print(f'I am {self.age} years old')


person1 = Human('John', 34)
person2 = Human('Jane', 23)
# print(person1.name, person1.age)
# print(person2.name, person2.age)
# person1.surname = 'Colt'
# print(person1.name, person1.surname)

# person1.say_info()
# person2.say_info()

person1.life_length()
person2.life_length()