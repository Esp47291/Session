from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass


class Book(AbstractProduct):
    def __init__(self, title: str, quantity: int, price: float, author: str):
        self.title = title
        self.quantity = quantity
        self.price = price
        self.author = author

    def get_description(self) -> str:
        return f"Книга: {self.title}, Автор: {self.author}"


book = Book("Война и мир", 5, 500, "Лев Толстой")
print(book.get_description())