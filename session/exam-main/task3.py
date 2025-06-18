from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass


class Product(AbstractProduct):
    def __init__(self, title: str, quantity: int, price: float):
        self.title = title
        self.quantity = quantity
        self.set_price(price)

    def get_price(self) -> float:
        return self._price

    def set_price(self, new_price: float):
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self._price = new_price


class Book(Product):
    def __init__(self, title: str, quantity: int, price: float, author: str):
        super().__init__(title, quantity, price)
        self.author = author

    def get_description(self) -> str:
        return f"Книга: {self.title}, Автор: {self.author}"


try:
    book = Book("Война и мир", 5, 500, "Лев Толстой")
    print(book.get_description())
    print("Текущая цена:", book.get_price())  # 500

    book.set_price(450)
    print("Обновлённая цена:", book.get_price())  # 450

    book.set_price(-100)
except ValueError as e:
    print("Ошибка:", e)