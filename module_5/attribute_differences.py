# Различие атрибутов класса и экземпляра. Пространство имен класса

class Human:
    head = True

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

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __str__(self):
        return self.name


person1 = Human('John', 34)
person2 = Human('Jane', 23)
print(Human.head)