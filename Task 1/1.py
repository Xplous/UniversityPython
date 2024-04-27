while(True):
    try:
        value = input();
        if (value == "exit"):
            break
        print(len(value))
    except ValueError:
        print("Ошибка! Несоответствие типа данных")
        break



