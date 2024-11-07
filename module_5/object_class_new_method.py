# Класс object и метод __new__

class User:
    __instance = None

    def __new__(cls, *args, **kwargs):
        print('I in new')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print('I in init')
        self.args = args
        # self.kwargs = kwargs
        # self.name = kwargs.get('name')
        # self.age = kwargs.get('age')
        for key, value in kwargs.items():
            setattr(self, key, value)


other = [1, 2, 3]
user = {'name': 'John', 'age': 35, 'city': 'Tokio'}

print(int.__mro__)
print(object)

# user1 = User(other, user, name='John', age=35)
user1 = User(*other, **user)
# user2 = User()
# print(User.__mro__)
# print(user1)
# print(user1 is user2)
print(user1.args)
# print(user1.kwargs)
print(user1.name)
print(user1.age)
print(user1.city)