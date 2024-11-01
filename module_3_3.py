def print_params(a = 1, b = 'строка', c = True, d = 13 , f  = 88 , g = 90):
    print( a, b, c, d , f , g)

values_list_2 = ["off", 1399, "man", 647]
values_list = [135, 'bb', "Olonso"]
values_dict = {'d' : 1, 'f' : "Flora",'g': False}
# print_params(*values_list)
# print_params(**values_dict)
# print_params(b = 25)
# print_params(c = [1,2,3])
# print_params()
# print_params(*values_list,**values_dict)
print_params(*values_list_2, 42, False)
