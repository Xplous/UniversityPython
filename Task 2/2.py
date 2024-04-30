str = input("Введите слово: ").upper()
symbol = input("Введите символ: ")
count = 0;
for i in str:
    if symbol.upper() == i:
        count += 1
result = {symbol: count}
print(result)