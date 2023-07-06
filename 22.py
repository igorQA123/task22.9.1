def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину последовательности
    if array[middle-1] < element <= array[middle]:  # если элемент в середине,
        return middle-1  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

array = list(map(int,input("Введите несколько целых чисел через пробел ").split()))



element = int(input("Введите любое случайное число в диапазоне чисел введенных ранее "))

array = sorted(array)
left = int(array[0])
right = int(array[-1])

if element < left or element > right:
    print('Числа нет в диапазоне')
else:
    print('индекс числа последовательности, которое меньше введенного =', binary_search(array, element, 0, len(array) - 1))
    print('отсортированная введенная последовательность', array)