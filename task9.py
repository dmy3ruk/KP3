def task_9():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    count = 0
    for num in [a, b, c]:
        if num.is_integer():
            count += 1
    print("Кількість цілих чисел:",count)
print(task_9())