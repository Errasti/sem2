def create_sequence(n):
    temp_list = []
    for i in range(-n, n + 1):
        temp_list.append(i)
    return temp_list


def show_mult(a,b,user_list):
    user_mult = 0
    user_mult = user_list[a] * user_list[b]
    return user_mult


user_n = int(input("Введите длину последовательности: "))
print(create_sequence(user_n))
user_a, user_b = (int(i) for i in input('Введите индексы для перемножения ').split())
print(show_mult(user_a, user_b, create_sequence(user_n)))

