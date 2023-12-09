exp = 2+2==5

print (exp)
age = 8
if age == 8:
    print('тебе 8')
if age > 8:
    print('тебе больше 8 ')
if age >= 8:
    print('тебе 8 ')
if age != 8:
    print('тебе не 8')
if age < 8:
    print('тебе меньше 8 ')
if age <= 8:
    print('тебе меньше 8 или 8 ')
temp =int(input('введите температуру'))
if temp < 0:
    print('Холодно')
elif temp < 10:
    print('Прохладно')
elif temp < 29:
    print("тепло")
elif temp < 35:
    print("жарко")
else:
    print("очень жарко")
number =int(input("Введите число:"))
if number % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")