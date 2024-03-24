def task_6():
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))

    max_num=max(a, b)
    if a!=b:
        a=max_num
        b=max_num
        return a,b
    else :
        a=0
        b=0
        return a,b

print(task_6())