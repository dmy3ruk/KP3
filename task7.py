def task_6():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    count = 0
    for num in [a, b, c]:
        if num < 0:
            count += 1
    print(count)
print(task_6())