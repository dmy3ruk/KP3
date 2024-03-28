import math


def task_2():
    x1 = float(input("Введіть координату x1 точки: "))
    y1 = float(input("Введіть координату y1 точки: "))

    x2 = float(input("Введіть координату x2 точки: "))
    y2 = float(input("Введіть координату y2 точки: "))
    distance1 = math.sqrt(x1 ** 2 + y1 ** 2)
    distance2 = math.sqrt(x2 ** 2 + y2 ** 2)
    if(distance1 > distance2):
        print("перша точка ближча до координат")
    else:print("друга точка ближча до координат")
print(task_2())