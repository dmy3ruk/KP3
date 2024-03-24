def task_5():
    x= int(input("Enter x coordinate: "))
    y= int(input("Enter y coordinate: "))
    if x==0 and y==0:
        print("Точка на початку координат")
    else:
        return print(f"Точка знаходиться в  {'I' if x > 0 and y>0 else 'II' if y > 0 and x<0 
        else 'III' if x < 0 and y<0 else 'IV'} чверті координат")
print(task_5())