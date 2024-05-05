# Задание №1
# Упражнение на написание генераторов списков и словарей:
# 1. Создайте список квадратов первых 10 натуральных чисел, используя list comprehensions.

list_kvadrad = [int(i) ** 2 for i in range(10)]


# 2. Создайте словарь, содержащий названия дней недели и их порядковые номера, используя dict comprehension.
# Для дней недели можно использовать список ["Понедельник", "Вторник" и т.д.]

days = ["Понедельник", "Вторник","Среда","Четверг","Пятница","Суббота", "Воскресенье"]

dicts_days = {i:days[i]for i in range(len(days))}

# 3. Создайте множество, содержащее теги библиотек в нижнем регистре, используя list comprehension.
# Исходный список ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]

library_spisok = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
set_library = set(i.lower() for i in library_spisok)

print(list_kvadrad,dicts_days,set_library)