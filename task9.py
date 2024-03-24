def task_9():
    a=input("Enter first number: ")
    b=input("Enter second number: ")
    c=input("Enter third number: ")
    count = 0
    for num in [a, b, c]:
        if num.is_integer():
            count += 1
    print(count)
print(task_9())