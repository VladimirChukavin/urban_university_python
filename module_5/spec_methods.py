# Специальные методы классов

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

    def __len__(self):
        return self.age

    def __del__(self):
        print(f'{self.name} was deleted')


person1 = Human('John', 34)
person2 = Human('Jane', 23)
# del person1
person1.life_length()
person2.life_length()
# input()
print(len(person1))
print(len(person2))
