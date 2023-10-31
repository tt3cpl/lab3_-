def distance(point):
    x, y = point
    return x**2 + y**2  # функция для вычисления расстояния от точки до начала координат

def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # выбор опорного элемента
    left = [x for x in arr if key(x) < key(pivot)]  # элементы, меньшие опорного
    middle = [x for x in arr if key(x) == key(pivot)]  # элементы, равные опорному
    right = [x for x in arr if key(x) > key(pivot)]  # элементы, большие опорного
    return quick_sort(left, key) + middle + quick_sort(right, key)  # рекурсивно сортируем левую, среднюю и правую части

def find_k_closest_points(points, k):
    sorted_points = quick_sort(points, key=distance)  # сортировка точек с использованием быстрой сортировки
    return sorted_points[:k]  # возвращаем k ближайших точек

with open("input_8.txt", "r") as file:
    n, k = map(int, file.readline().split())  # считываем количество точек и k
    points = [list(map(int, line.split())) for line in file]  # считываем координаты точек

closest_points = find_k_closest_points(points, k)  # находим k ближайших точек

with open("output_8.txt", "w") as file:
    for i, point in enumerate(closest_points):
        file.write(f"[{point[0]}, {point[1]}]")  # записываем координаты точки
        if i < k - 1:
            file.write(", ")  # добавляем запятую, если точка не последняя
