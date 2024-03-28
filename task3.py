def task_3():
    angle1 = int(input("Введіть значення кута 1: "))
    angle2 = int(input("Введіть введіть значення кута 2: "))
    angle3=180-angle1-angle2
    if(angle3>0):
        print("Такий трикутник існує")
        if(angle1==90 or angle2==90 or angle3==90):
            print("цей трикутник є прямокутним")
print(task_3())