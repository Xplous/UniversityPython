import unittest
import time
import sys

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorialFunction(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_of_negative_input(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_of_large_input(self):
        with self.assertRaises(ValueError):
            factorial(1000000)

if __name__ == '__main__':
    start_time = time.time()
    unittest.main()
    end_time = time.time()
    print(f"Время выполнения тестов: {end_time - start_time} секунд")
