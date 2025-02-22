# Домашнее задание по теме "Режимы открытия файлов"


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, "r")
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        products_list = self.get_products()
        for product in products:
            if product.name not in products_list:
                file = open(self.__file_name, "a")
                file.write(f"{product.name}, {
                           product.weight}, {product.category}\n")
                file.close()
            else:
                print(f"Продукт {product.name} уже есть в магазине")


s1 = Shop()
p1 = Product("Potato", 50.5, "Vegetables")
p2 = Product("Spaghetti", 3.4, "Groceries")
p3 = Product("Potato", 5.5, "Vegetables")

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
