def fact(n):
    factorial = 1
    temp_list = []
    for i in range(2, n+1):
        temp_list.append(factorial)
        factorial *= i
    return temp_list


user_number = int(input("Введите N: ")) + 1
print(fact(user_number))
