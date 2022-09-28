def sequence(n):
    temp_list = []
    sequence_sum = 0
    for i in range(1, n+1):
        temp_list.append((1 + 1 / i) ** i)
    return temp_list


def show_sum(user_list):
    sequence_sum = 0
    for i in user_list:
        sequence_sum += i
    return round(sequence_sum, 3)


user_n = int(input('Введите N: '))
print(show_sum(sequence(user_n)))
