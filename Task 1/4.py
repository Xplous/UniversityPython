ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
hod = input().upper()
if (hod in ship):
    print("Попал")
else:
    print("Не попал")

name,lastname,age = input(),input(),input()
print(f"Ваше имя: {name}, фамилия: {lastname}, возраст: {age} лет.")
