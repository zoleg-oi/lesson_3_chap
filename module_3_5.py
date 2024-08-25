# Рекурсивное умножение цифр
def get_multiplied_digits(number):
    # проверим параметр
    if type(number) == int:
        str_number = str(number)
        first = int(str_number[0:1])
    else:
        return "Введите целое число"
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
