import random


def partition(arr, low, high):
    pivot = arr[high]  # выбираем опорный элемент (последний элемент в подмассиве)
    i = low - 1  # инициализируем индекс i

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1  # увеличиваем индекс i, если текущий элемент меньше опорного
            arr[i], arr[j] = arr[j], arr[i]  # меняем местами элементы в массиве

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # меняем местами опорный элемент и элемент на позиции (i+1)
    return i + 1  # возвращаем индекс опорного элемента после разделения

def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot = random_partition(arr, low, high)  # выбираем рандомизированный опорный элемент
        randomized_quick_sort(arr, low, pivot - 1)  # рекурсивно сортируем левую часть массива
        randomized_quick_sort(arr, pivot + 1, high)  # рекурсивно сортируем правую часть массива

def random_partition(arr, low, high):
    pivot_index = random.randint(low, high)  # генерируем рандомный индекс опорного элемента
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]  # меняем местами опорный элемент и элемент на рандомной позиции
    return partition(arr, low, high)  # вызываем partition для разделения


def quick_sort(arr):
    randomized_quick_sort(arr, 0, len(arr) - 1)  # начальные значения: low = 0, high = len(arr) - 1


with open('input_1.txt', 'r') as file:
    n = int(file.readline().strip())  # считываем количество элементов
    list = list(map(int, file.readline().split()))  # считываем элементы массива


quick_sort(list)

with open('output_1.txt', 'w') as file:
    file.write(' '.join(map(str, list)))  # преобразуем массив в строку и записываем в файл
