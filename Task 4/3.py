# Задание №3
# Создайте функцию, которая принимает аргументы «текст» и «имя файла».
# Функция должна записать в файл (если файла не существует, то создать его) текст с новой строки. Выведите информацию из четных строк файла.

def write_file(text, filename):
    f = open(filename,"a+")
    f.write(text + '\n')
def read_file(filename):
    try:
        f = open(filename,"r")
        lines = f.readlines()
        strok = [lines[i].strip() for i in range(1,len(lines),2)]
        print(strok)
    except FileNotFoundError:
        print("Файл не найден!")
def example():
    write_file("питончик 1","example.txt")
    write_file("питончик 2","example.txt")
    write_file("питончик 3","example.txt")
    write_file("питончик 4","example.txt")
    read_file("example.txt")
example()