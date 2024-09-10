# "Раз, два, три, четыре, пять .... Это не всё?"
list_all = []


def calculate_structure_sum(list_data):
    global list_all
    for ld in list_data:
        if (isinstance(ld, str) == False) and (isinstance(ld, int) == False):
            if isinstance(ld, dict) == True:  # Словарь разберем отдельно
                # да можно написать проверку по полученным типам ключей и значений,
                # но, судя по заданию, этот момент можно упустить.
                key_dc = ld.keys()
                for dc in key_dc:
                    list_all.append(len(dc))
                val_dc = ld.values()
                for vdc in val_dc:
                    list_all.append(vdc)
                continue
            if len(ld) == 0:  # Проверим на пустое значение
                continue
            calculate_structure_sum(ld)
        elif isinstance(ld, str) == True:
            list_all.append(len(ld))
        elif isinstance(ld, int) == True:
            list_all.append(ld)
    return sum(list_all)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
