# Однокоренные
##
# ****************
# Для наглядности можно ввести еще один параметр, который позволяет переключать механизм
# выполнения функции
# ниже решение задачи как указано в задании.
def single_root_words_ower(metod, root_word, *other_words):
    # метод решения зависит от переданного параметра
    # 0 - используем оператор in
    # 1 - используем метод find()
    # 2 - используем метод index()
    same_words = []
    root_word = root_word.lower()

    if metod == 0:
        print()
        print('Используем оператор - in')
        for i in range(len(other_words)):
            ow = other_words[i].lower()
            # поищем не входит ли root в элемент последовательности
            if ow in root_word:  same_words.append(other_words[i])
            # а теперь наоборот не входит ли элемент в root
            if root_word in ow:  same_words.append(other_words[i])
    if metod == 1:
        print()
        print('Используем метод - find()')
        for i in range(len(other_words)):
            ow = other_words[i].lower()
            # поищем не входит ли root в элемент последовательности
            if root_word.find(ow) != -1:  same_words.append(other_words[i])
            # а теперь наоборот не входит ли элемент в root
            if ow.find(root_word) != -1:  same_words.append(other_words[i])
    if metod == 2:
        print()
        print('Используем метод - index()')
        for i in range(len(other_words)):
            ow = other_words[i].lower()
            try:
                root_word.index(ow)
            except:
                continue #ничего не делаем
            else:
                same_words.append(other_words[i])
            try:
                ow.index(root_word)
            except:
                continue #ничего не делаем
            else:
                same_words.append(other_words[i])

    return same_words


result1 = single_root_words_ower(1, 'rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words_ower(2, 'Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)
result3 = single_root_words_ower(0, 'Ablemable', 'Able', 'Mable', 'Disable', 'Bagel')
print(result3)
print()

print('Решение, указанное в задании')
print()


def single_root_words(root_word, *other_words):  # функция использует оператор in
    same_words = []
    root_word = root_word.lower()
    for i in range(len(other_words)):
        ow = other_words[i].lower()
        # поищем не входит ли root в элемент последовательности
        if ow in root_word:  same_words.append(other_words[i])
        # а теперь наоборот не входит ли элемент в root
        if root_word in ow:  same_words.append(other_words[i])

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
