def task_1():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    return (a ** 2 if a >= 0 else a ** 4,
            b ** 2 if b >= 0 else b ** 4,
            c ** 2 if c >= 0 else c ** 4)
print(task_1())