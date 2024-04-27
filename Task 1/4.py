ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
array = ship.split(" ")
hod = input().upper()
print(hod,array)
for i in array:
    if (hod in i):
        print("Попал")
        flag = True
        break
else:
    print("Не попал")

name,lastname,age = input(),input(),input()
print(f"Ваше имя: {name}, фамилия: {lastname}, возраст: {age} лет.")