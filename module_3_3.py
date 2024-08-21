# Распаковка позиционных параметров
def print_params(a=1, b='строка', c=True):
    # преобразование типа строка тв строку не возбраняется
    # но можно, конечно, устроить проверку типов и исключить преобразование строки в строку.
    # например

    if type(a) != str:
        a = str(a)
    if type(b) != str:
        b = str(b)
    if type(c) != str:
        c = str(c)

    print(a + ' ' + b + ' ' + c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['Дом', 7, True]
print_params(*values_list)
value_dic = {'a': 8, 'b': False, 'c': 'Садик'}
print_params(**value_dic)
values_list_2 = [75.68, 'Зима']
print_params(*values_list_2, True)
