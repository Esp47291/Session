from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass


class Product(AbstractProduct):
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.set_price(price)

    def get_price(self) -> float:
        return self._price

    def set_price(self, new_price: float):
        if new_price < 0:
            raise ValueError("Цена не может быть меньше нуля!")
        self._price = new_price

    def __add__(self, other):
        if isinstance(other, Product):
            total_quantity = self.quantity + other.quantity
            weighted_price = (self.get_price() * self.quantity + other.get_price() * other.quantity) / total_quantity
            return Product(f"{self.name} + {other.name}", total_quantity, weighted_price)
        else:
            raise TypeError("Можно складывать только объекты Product")

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.get_price() < other.get_price()
        else:
            raise TypeError("Можно сравнивать только объекты Product")

    def __gt__(self, other):
        if isinstance(other, Product):
            return self.get_price() > other.get_price()
        else:
            raise TypeError("Можно сравнивать только объекты Product")

    def __str__(self):
        return f"{self.name} (Количество: {self.quantity}, Цена: {self.get_price()})"


class Book(Product):
    def __init__(self, name: str, quantity: int, price: float, author: str):
        super().__init__(name, quantity, price)
        self.author = author

    def get_description(self) -> str:
        return f"Книга: {self.name}, Автор: {self.author}"

    def __str__(self):
        return f"{self.name}, Автор: {self.author} (Количество: {self.quantity}, Цена: {self.get_price()})"


class Laptop(Product):
    def __init__(self, name: str, quantity: int, price: float, brand: str):
        super().__init__(name, quantity, price)
        self.brand = brand

    def get_description(self) -> str:
        return f"Ноутбук: {self.name}, Бренд: {self.brand}"

    def __str__(self):
        return f"{self.name}, Бренд: {self.brand} (Количество: {self.quantity}, Цена: {self.get_price()})"


# Пример использования
try:
    book1 = Book("Война и мир", 5, 500, "Лев Толстой")
    book2 = Book("Преступление и наказание", 3, 450, "Фёдор Достоевский")

    print(book1 + book2)
    # Вывод: Война и мир + Преступление и наказание Количество: 8, Цена: 481.25

    print(book1 > book2)  # True
    print(book1 < book2)  # False

    invalid_book = Book("Ошибка", 1, -100, "Автор")  # Вызовет ValueError

except ValueError as e:
    print("Ошибка значения:", e)


# Проверка get_description
book = Book("Война и мир", 5, 500, "Лев Толстой")
print(book.get_description())  # Книга: Война и мир, Автор: Лев Толстой