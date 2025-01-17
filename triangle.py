def area(a, h):
    '''
    параметры:
    a (float, int): сторона треугольнаа (число)
    h (float, int): высота к стороне a (число)
    возвращаемое значение:
    площадь треугольника по формуле через сторону и прилежащую к ней высоту

    при вводе отрицательных чисел выводит ошибку
    '''
    if isinstance (a, str) or isinstance (h, str):
        return 'Вы ввели строку'
    if a < 0 or h < 0:
        return 'Сторона или высота треугольника не может быть отрицательным числом'
    return a * h / 2

def perimeter(a, b, c):
    '''
    параметры:
    a (int): сторона треугольника (число)
    b (int): сторона треугольника (число)
    c (int): сторона треугольника (число)
    возвращаемое значение:
    сумма сторон (периметр треугольника) по формуле трех сторон

    при вводе отрицательных или нулевых чисел выводит ошибку
    '''
    if isinstance (a, str) or isinstance (b, str) or isinstance (c, str):
        return 'Вы ввели строку'
    if a <= 0 or b <= 0 or c <= 0:
        return 'Сторона треугольника не может быть отрицательным числом или нулем'
    return a + b + c
