#def get_stone(n,one_stone):
first_num = 1
second_num = 1
result = []
n = 400
one_stone = 20

for i in range(1,n+1):

    # переберает с 1 до 20
    if one_stone % (first_num + second_num) == 0 and first_num != second_num and  first_num < second_num:
        print(f'Когда первое число {first_num}, а второе {second_num} то- подходит, подходит')
        result.append(f'{one_stone}-{first_num}{second_num}')
        second_num += 1
    elif second_num == 20:
        print(f'Когда первое число {first_num}, а второе {second_num} то- НЕ подходит, идем дальше')
        first_num += 1
        second_num -= 19
    else:
        print(f'Когда первое число {first_num}, а второе {second_num} то-НЕ подходит, идем дальше')
        second_num += 1


#result = get_stone(400,19)
print(result)