book1 = ("Война и мир", 5, 500, "Лев Толстой")  # можно сделать с input немного не понимаю цель задания(
book2 = ("Преступление и наказание", 3, 450, "Фёдор Достоевский")
print (f" {book1[0]} + {book2[0]}   (Количество: {book1[1] + book2[1]}, + Цена: {book1[2] + book2[2]})")

if book1[2] > book2[2]:
    print("True")
else:
    print("False")

    try:
        if book1[2] or book2[2] < 0:
            print("invalid_book")
    except ValueError:
        print("Ошибка значения")

