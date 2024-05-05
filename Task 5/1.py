# Вариант 3
# Встроенные модули
# Задание 1
from random import shuffle
from modules import circle_area, average_grade, sberbank_shares


# Пункт 1
def mix(spisok: list) -> list:
    shuffle(spisok)
    return spisok

data = [1, 2, 3, 4, "12312"]
print("Перемешанный список:", mix(data))

# Пункт 2

radius = 5
area = circle_area(radius)
print("Площадь круга:", area)

scores = [4, 5, 3, 4, 5]
average = average_grade(scores)
print("Средний балл:", average)

money = 5000
shares = sberbank_shares(money)
print("Количество ценных бумаг Сбербанка:", shares)