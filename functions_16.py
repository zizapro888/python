import random 
inventory = []

def gaw():
    print("Гав-гав-гав!")


def robot_forward():
    print("Робот идет вперед")


def robot_backward():
    print("Робот идет назад")


def robot_left():
    print("Робот идет влево")


def robot_right():
    print("Робот идет вправо")

def robot_scan():
    items = ["Ветка", "Бутылка", "Железо", "Дерево"]
    item = random.choice(items)
    print(f"Робот нашел предмет {item}")
    return item


def robot_pickup(item):
    global inventory
    inventory.append(item)

def check_inventory():
    for index, item in enumerate(inventory, start=1):
        print(f"{index}. {item}")
def  craft():
    recept1 = ["железо , "лава ,"камень"] # ядро земли
    recept2 = ["кварц" , "вода" ,"человек"] # скибиди туалет
    recept3 =["ядро земли" , "газ" "звезды"] # земля
    recepts = [recept1, recept2, recept3,]
    recept_names =["ядро земли", "скибиди туалет", "земля"]
    print("Доступны следующие рецепты:")
    for index,recept in enumerate(recept_names,  start=1):
        print(f"{index}. {recept}")
    choice = input('Выбери, что хочешь крафтить')
    if not choice.isdigit():
        print('Вводиьб можно только числа')    
        return None
    choice = int(choice) - 1
    if choice not in range(0, len(recept_names)):
        print('Рецепта с таким номером нет')
        return None
    choice_recept = recept_names[choice]
    print(f"Вы выбрали крафтить {choice_recept}")
    ingredients = recept[choice]
    print(f'Ингердиенты: {ingredients}')
    print(f"Уничтожен {item}")
    inventory.remove(item)
    ingredients.remove(item)
    if not ingredients:
        inventory.append(choice)
               
while True:
    key = input("Введите клавишу: ")
    if key == "w":
        robot_forward()
    elif key == "s":
        robot_backward()
    elif key == "a":
        robot_left()
    elif key == "d":
        robot_right()
    elif key == "f":
        item = robot_scan()
        robot_pickup(item)
        print(inventory)
    elif key == 'c':
        craft()
        
