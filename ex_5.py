# Функция для быстрой сортировки
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[len(arr) // 2]  # выбираем опорный элемент (середину массива)
    left = [x for x in arr if x < p]  # создаем список элементов меньших опорного
    middle = [x for x in arr if x == p]  # создаем список элементов равных опорному
    right = [x for x in arr if x > p]  # создаем список элементов больших опорного
    return quicksort(left) + middle + quicksort(right)  # рекурсивно сортируем и объединяем списки

# Функция для вычисления индекса Хирша
def hindex(citations):
    citations = quicksort(citations)  # сортировка массива цитирований

    n = len(citations)  # получаем количество элементов в массиве
    h = 0  # инициализируем индекс Хирша

    # начинаем итерацию с конца отсортированного массива
    for i in range(n, 0, -1):
        if citations[n - i] >= i:
            # если количество цитирований на позиции n - i (нумерация с 0) больше или равно i,
            # это означает, что есть как минимум i статей с i или более цитированиями.
            # поэтому устанавливаем индекс Хирша равным i и завершаем цикл.
            h = i
            break

    return h  # возвращаем вычисленный индекс Хирша


# считываем входные данные из input.txt
with open("input_5.txt", "r") as file:
    citations = list(map(int, file.readline().strip().split(',')))  # читаем и преобразуем строку с цитированиями в список целых чисел

# вычисляем индекс Хирша
h_index = hindex(citations)
 
# записываем результат в output.txt
with open("output_5.txt", "w") as file:
    file.write(str(h_index))  # записываем значение индекса Хирша в файл output.txt
