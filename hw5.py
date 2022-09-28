def mix_list(user_list):
    temp_value = 0
    for i in range(0, len(user_list) // 2):
        temp_value = user_list[i]
        user_list[i] = user_list[len(user_list) // 2 + i]
        user_list[len(user_list) // 2 + i] = temp_value
    return user_list


def create_sequence(n):
    temp_list = []
    for i in range(-n, n + 1):
        temp_list.append(i)
    return temp_list


n = int(input('Введите длину последовательности N: '))
print(create_sequence(n))
print(mix_list(create_sequence(n)))
