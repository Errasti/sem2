def sum_num(num):
    sum_numbers = 0
    for i in str(num):
        if i != '.':
            sum_numbers += int(i)
    return sum_numbers


n = input("Введите число: ")
print(sum_num(n))

