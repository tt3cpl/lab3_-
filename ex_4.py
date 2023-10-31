def count_points_in_segments(segments, points):
    
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2][1]  # выбираем опорный элемент (конечную точку отрезка)
        left = [x for x in arr if x[1] < pivot]  # отделяем элементы, меньшие опорного
        middle = [x for x in arr if x[1] == pivot]  # отделяем элементы, равные опорному
        right = [x for x in arr if x[1] > pivot]  # отделяем элементы, большие опорного
        return quick_sort(left) + middle + quick_sort(right)  # рекурсивно сортируем левую, среднюю и правую части

    # сортируем отрезки с использованием быстрой сортировки
    segments = quick_sort(segments)

    result = [0] * len(points)  # инициализируем список результатов нулями

    for i, point in enumerate(points):
        count = 0
        for segment in segments:
            if segment[0] <= point <= segment[1]:  # проверяем, входит ли точка в текущий отрезок
                count += 1
            if point <= segment[1]:  # если текущая точка меньше или равна конечной точке отрезка, выходим из цикла
                break
        result[i] = count  # записываем количество отрезков, в которые входит данная точка в результат

    return result

# считываем входные данные из файла
with open("input_4.txt", "r") as file:
    s, p = map(int, file.readline().split())  # считываем количество отрезков и точек
    segments = [tuple(map(int, file.readline().split())) for _ in range(s)]  # считываем отрезки
    points = list(map(int, file.readline().split()))  # считываем точки

# вычисляем результат
result = count_points_in_segments(segments, points)

# записываем результат в файл
with open("output_4.txt", "w") as file:
    file.write(" ".join(map(str, result)))  # записываем результат в файл
