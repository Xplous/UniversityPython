value = int(input())
array = [i for i in range(-value, value+1)]
print(array)
negative_array = [i for i in array if i < 0]
positive_array = [i for i in array if i > 0]
print("Сумма отрицательных чисел", sum(negative_array))
print("Сумма положительных чисел", sum(positive_array))
