def task_1(a,b,c):
    return (a ** 2 if a >= 0 else a ** 4,
            b ** 2 if b >= 0 else b ** 4,
            c ** 2 if c >= 0 else c ** 4)
print(task_1(2,-3,4))