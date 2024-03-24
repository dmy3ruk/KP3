def task_8():
    a=input("Enter first number: ")
    b=input("Enter second number: ")
    c=input("Enter third number: ")
    count = 0
    for num in [a, b, c]:
        if num > 0:
            count += 1
    print(count)
print(task_8())