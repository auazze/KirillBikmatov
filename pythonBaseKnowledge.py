# иду по роад мапу с сайта roadmap.sh

# 1. Базовый синтаксис пропустим

# 2. Переменные
def variables():
    """
    Переменные
    """
    print(variables.__doc__)
    var_x = 5
    var_y = "55"
    var_i = str(var_x)
    var_j = int(var_y)
    print(f"Тип x: {type(var_x)}\nТип y: {type(var_y)}\nВозвращаем обратно тип i: {type(int(var_i))}\nВозвращаем обратно тип j: {type(str(var_j))}")

variables()

# 3. Условия
def conditions():
    """
    Условия
    """
    print(conditions.__doc__)
    cond_x = 1
    cond_y = 2
    cond_z = 100

    if cond_z > cond_x or cond_y:
        pass

    if cond_y > cond_x:
        print("y > x")
    else:
        print("x > y")

    print("z > x and y") if cond_z > cond_x and cond_y else print("z < x and y")

conditions()

# 4. Циклы
def loops():
    """
    Циклы
    """
    print(loops.__doc__)
    print("\nwhile Loop")
    loops_i = 0
    loops_j = 100
    while loops_i < loops_j:
        print(loops_i)
        loops_i += 10
        if loops_i == 50:
            continue
    else:
        print("i not bigger than j")


    # while True:
    #     response = input("Say something :) (\"Bye\" for exit)\n")
    #     if response == "Bye":
    #         break

    print("\nfor Loop")
    for for_item in [1, 2, 3, 4, 5]:
        print(for_item)

loops()

# 5. Type Cast тоже мимо

# 6. Исключения
def exceptions():
    try:
        print("I tried")
    except Exception:
        print("Oops... Exception")
