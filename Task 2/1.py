len_elements = int(input("Кол-во элементов: "))
array = [input("Элемент: ") for i in range(len_elements)]
new_array = []
n = int(input("Степень: "))
for i in array:
    try:
        new_array.append(int(i) ** n)
    except ValueError:
        new_array.append(i * n)
print(new_array)