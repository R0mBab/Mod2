print('Сейчас нужно ввести 3 числа, по очереди')
print('жду первое')
first = int(input())
print('жду второе')
second = int(input())
print('жду третье')
third = int(input())
print(first,second,third)
if first==second==third:
    print('Введеных равных чисел 3')
elif first==second or second==third or first==third:
    print('Введеных равных чисел 2')
else:
    print('Введеных равных чисел 0')
