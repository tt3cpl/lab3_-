def anti_quick_sort(n):
    arr = [0] * n  # создаем массив длиной n, заполненный нулями
    for i in range(n):
        arr[i] = i + 1  # заполняем массив числами от 1 до n

    for i in range(2, n):
        arr[i], arr[i // 2] = arr[i // 2], arr[i]  # меняем элементы массива для "переворачивания" его структуры
    arr_res = []
    for i in arr:
        arr_res.append(i)  # создаем новый массив с теми же элементами
    return arr_res  # возвращаем перевернутый массив

with open('input_2.txt') as f:
    n = int(f.readline())  # считываем количество элементов в массиве из файла input_2.txt

with open('output_2.txt', 'w') as f:
    f.write(f"{anti_quick_sort(n)}")  # записываем результат выполнения функции anti_quick_sort в файл output_2.txt


