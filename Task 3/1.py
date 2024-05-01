def add(numbers):
    print("-" * 25)
    return sum(numbers)


def sub(numbers):
    print("-" * 25)
    return numbers[0] - sum(numbers[1:])


def mult(numbers):
    print("-" * 25)
    return eval('*'.join(map(str, numbers)))


def div(numbers):
    expression = '/'.join(map(str, numbers))
    print("-" * 25)
    try:
        result = eval(expression)
    except ZeroDivisionError:
        print("Error:", "Делить на 0 нельзя")
        result = None
    return result



def exponent(numbers):
    print("-"* 25)
    return eval('**'.join(map(str, numbers)))


def validate_input(numbers):
    if all(isinstance(num, (int, float)) for num in numbers):
        return True
    else:
        raise ValueError("Значения должны быть цифрами")


while True:
    print("Список операций")
    print("(-) Вычитание чисел")
    print("(+) Сложение чисел")
    print("(*) Умножение чисел")
    print("(/) Деление чисел")
    print("(^) Возвести в степень числа")
    print("(exit) Выход из программы")

    num_operation = input("Введите номер операции: ")

    if num_operation == 'exit':
        print("-" * 55)
        print("Спасибо за использование лучшего калькулятора EVER :>")
        print("-" * 55)
        break

    operations = {
        '-': sub,
        '+': add,
        '*': mult,
        '/': div,
        '^': exponent
    }

    if num_operation not in operations:
        print("-" * 25)
        print("Ошибка! Выберите номер операции от 1 до 6 ;]")
        print("-" * 25)
        continue
    try:
        numbers = [float(num) for num in input("Введите числа через пробел: ").split()]
        validate_input(numbers)
    except ValueError:
        print("-" * 25)
        print("Ошибка! Вы пытаетесь преобразовать строку в число :)")
        print("-" * 25)
        continue

    print("Результат:", operations[num_operation](numbers))
    print("-" * 25)
