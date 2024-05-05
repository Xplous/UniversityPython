def log_call_info(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} была вызвана с позиционными аргументами: {args} и именованными аргументами: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_call_info
def fibonacci(n):
    fibonachi = [0, 1]

    [fibonachi.append(fibonachi[k-1] + fibonachi[k-2]) for k in range(2, n)]

    return fibonachi

n = int(input("Введите конечное число коллекции: "))
result = fibonacci(n)
print(result)
