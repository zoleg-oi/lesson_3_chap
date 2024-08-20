# Счётчик вызовов
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string=''):
    count_calls()
    r_str = []
    r_str.append(len(string))
    r_str.append(string.upper())
    r_str.append(string.lower())
    return tuple(r_str)


def is_contains(string='', list=[]):
    count_calls()

    for i in range(0, len(list)):
        string = string.lower()
        ii = list[i].lower()
        #        if ii.find(string) != -1: # елси потребуется найти подстроку в списке,
        #        но нужна строка целиком по условию, хотя работать будет и в таком виде
        # это решение по заданию - буквально
        if string == ii:
            ret_i = True
        else:
            ret_i = False
    return ret_i


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
