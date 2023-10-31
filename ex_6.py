def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # возвращаем массив, если он содержит 1 элемент или пустой

    pivot = arr[len(arr) // 2]  # выбираем опорный элемент из середины массива
    less = [x for x in arr if x < pivot]  # создаем массив меньших элементов
    equal = [x for x in arr if x == pivot]  # создаем массив элементов, равных опорному
    greater = [x for x in arr if x > pivot]  # создаем массив больших элементов

    return quick_sort(less) + equal + quick_sort(greater)  # рекурсивно сортируем меньшие и большие элементы, объединяем с опорным

# чтение входных данных
with open("input_6.txt", "r") as file:
    n, m = map(int, file.readline().split())  # считываем два числа n и m из файла
    array_A = list(map(int, file.readline().split()))  # считываем массив array_A
    array_B = list(map(int, file.readline().split()))  # считываем массив array_B

    # создание массива C путем перемножения элементов из A и B
    array_C = [a * b for a in array_A for b in array_B]

    # выполняем быструю сортировку
    sorted_C = quick_sort(array_C)

    # вычисление суммы каждого десятого элемента
    sum_of_tenth_elements = sum(sorted_C[i] for i in range(0, len(sorted_C), 10))

# запись результата (суммы) в выходной файл
with open("output_6.txt", "w") as file:
    file.write(str(sum_of_tenth_elements))
