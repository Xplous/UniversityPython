from typing import List, Union
def mult(elements: List[Union[int, float]], multiplier: Union[int, float] = 2) -> List[Union[int, float]]:
    return [element * multiplier for element in elements]

mult_lambda = lambda elements, multiplier=2: [element * multiplier for element in elements]

elements = [float(num) for num in input("Введите числа через пробел: ").split()]

n = int(input("Введите степень: "))

print("Результат функции c введённой степенью:", mult(elements,n))
print("Результат функции по дефолту:", mult(elements))
print("Результат lamda-функции c введённой степенью:", mult_lambda(elements, n))
print("Результат lamda-функции по дефолту:", mult_lambda(elements))
