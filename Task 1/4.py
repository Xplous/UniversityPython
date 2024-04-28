ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
hod = input().upper()
try:
    hod = int(input) 
    print("Введите букву и цифру")
except ValueError:
    if (len(hod) == 2 & hod in ship):
       print("Попал")
    else:
       print("Не попал")

name,lastname,age = input(),input(),input()
print("Ваше имя: {name} , Фамилия: {lastname}, Возраст: {age}".format(age=age, name=name, lastname=lastname))
print(f"Ваше имя: {name}, фамилия: {lastname}, возраст: {age} лет.")
