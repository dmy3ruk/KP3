def task_4():
    num1= int(input("Введіть перше число:"))
    num2 = int(input("Введіть друге число:"))
    if(num1!=num2):
        if(num1>num2):
            num1=(num1*num2)*2
            num2=(num1+num2)/2

        elif(num1<num2):
            num1=(num1+num2)/2
            num2 = (num1 * num2) * 2
        print("Результат першого числа:",num1)
        print("Результат другого числа:", num2)

#print(tack_4())