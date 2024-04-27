from itertools import permutations
value = input()
try:
    array = [int(i) for i in value]
    print(array)
    l = list(permutations(array))
    print(l)
    if(len(value) != 3):
        print(f"Введённое число не трёхзначное. {value}")
    if(len(set(array)) != len(array)):
        print(f"В строке есть повторяющиеся цифры")
except ValueError:
    print("Введите трёхзначное число!")