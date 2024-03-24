def task_10():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    k = int(input("Enter divisor number: "))

    results = []

    if a % k == 0:
        results.append(a)
    if b % k == 0:
        results.append(b)
    if c % k == 0:
        results.append(c)

    print( "число", k, "є дільником таких чисел:", results)
print(task_10())