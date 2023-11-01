def partition(arr, low, high):
    # выбираем опорный элемент как медиану из трех: первого, среднего и последнего элементов
    middle = (low + high) // 2  # находим индекс среднего элемента
    if arr[low] > arr[middle]:  # проверяем, является ли первый элемент наименьшим из трех
        arr[low], arr[middle] = arr[middle], arr[low]  # если нет, меняем местами средний и первый элемент
    if arr[low] > arr[high]:  # проверяем, является ли первый элемент наименьшим из трех
        arr[low], arr[high] = arr[high], arr[low]  # если нет, меняем местами последний и первый элемент
    if arr[middle] > arr[high]:  # проверяем, является ли средний элемент наибольшим из трех
        arr[middle], arr[high] = arr[high], arr[middle]  # если нет, меняем местами последний и средний элемент
    
    pivot = arr[middle]  # опорным элементом будет средний из трех элементов
    
    i = low - 1  # индекс для меньших элементов
    j = high + 1  # индекс для больших элементов
    
    while True:
        i += 1  # увеличиваем индекс i
        while arr[i] < pivot:  # поиск элемента, который меньше опорного
            i += 1

        j -= 1  # уменьшаем индекс j
        while arr[j] > pivot:  # поиск элемента, который больше опорного
            j -= 1

        if i >= j:  # если индексы i и j пересеклись
            return j  # возвращаем индекс j, на котором разделены элементы

        arr[i], arr[j] = arr[j], arr[i]  # меняем элементы i и j местами

def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)  # вызываем функцию partition для разделения массива
        quick_sort(arr, low, partition_index)  # рекурсивно сортируем левую часть
        quick_sort(arr, partition_index + 1, high)  # рекурсивно сортируем правую часть


with open("input_1.txt", "r") as file:
    n = int(file.readline())  # читаем число элементов в массиве из файла
    arr = list(map(int, file.readline().split()))  # читаем массив из файла и преобразуем его в список целых чисел

quick_sort(arr, 0, n - 1)  # запускаем сортировку Quick Sort

with open("output_1.txt", "w") as file:
    file.write(" ".join(map(str, arr)))  # записываем отсортированный массив в файл
