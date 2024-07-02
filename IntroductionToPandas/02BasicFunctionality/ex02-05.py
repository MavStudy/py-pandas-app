# Pandas - Основная функциональность
#
# Приведем основные подходы к работе с данными,
# содержащимися в Series и DataFrame.
import pandas as pd
import numpy as np


def separator():
    print('-' * 70)


def arr_info(name, arr):
    print(
        f"Массив {name}:",
        type(arr),
        id(arr),
        arr.shape
        # arr.dtype
    )


def main():
    #  Применение функций и отображение
    #
    # Универсальные функции NumPy также работают с объектами pandas:
    frame = pd.DataFrame(np.random.randn(4, 3),
                         columns=list('bde'),
                         index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    arr_info('frame', frame)
    print(frame)
    # Массив frame: <class 'pandas.core.frame.DataFrame'> 41983904 (4, 3)
    #                b         d         e
    # Utah    1.877862 -0.373953 -0.447493
    # Ohio   -0.316602 -0.218644 -0.652199
    # Texas  -1.571244 -0.694143 -0.074198
    # Oregon  1.666556  2.064941 -0.374579

    separator()

    result1 = np.abs(frame)
    arr_info('result1', result1)
    print(result1)
    # Массив result1: <class 'pandas.core.frame.DataFrame'> 188658832 (4, 3)
    #                b         d         e
    # Utah    1.877862  0.373953  0.447493
    # Ohio    0.316602  0.218644  0.652199
    # Texas   1.571244  0.694143  0.074198
    # Oregon  1.666556  2.064941  0.374579

    separator()

    # Другой частой операцией является применение функции к одномерным
    # массивам для каждого столбца или строки. Метод apply объекта DataFrame
    # выполняет это:
    #
    # f = lambda x: x.max() - x.min()
    # result2 = frame.apply(f)
    result2 = frame.apply(lambda x: x.max() - x.min())
    arr_info('result2', result2)
    print(result2)
    # Массив result2: <class 'pandas.core.series.Series'> 31699248 (3,)
    # b    3.449106
    # d    2.759084
    # e    0.578001
    # dtype: float64

    # В результате мы получили объект Series, у которого индекс совпадает
    # со столбцами объекта DataFrame.

    separator()

    # Если задать параметр axis = ’columns’ в функции apply, функция будет
    # применяться к строкам:
    # result3 = frame.apply(f, axis='columns')
    result3 = frame.apply(lambda x: x.max() - x.min(), axis='columns')
    arr_info('result3', result3)
    print(result3)
    # Массив result3: <class 'pandas.core.series.Series'> 188660272 (4,)
    # Utah      2.325354
    # Ohio      0.433555
    # Texas     1.497045
    # Oregon    2.439520
    # dtype: float64

    separator()

    # Многие из наиболее распространенных статистических методов (например,
    # sum и mean) являются методами DataFrame, поэтому использование apply
    # не обязательно.

    # Функция, передаваемая в apply, не обязана возвращать скалярное значение,
    # она может также возвращать объект Series:
    arr_info('frame', frame)
    print(frame)
    # Массив frame: <class 'pandas.core.frame.DataFrame'> 41983904 (4, 3)
    #                b         d         e
    # Utah    1.877862 -0.373953 -0.447493
    # Ohio   -0.316602 -0.218644 -0.652199
    # Texas  -1.571244 -0.694143 -0.074198
    # Oregon  1.666556  2.064941 -0.374579

    separator()

    def f(x):
        return pd.Series([x.min(), x.max()], index=['min', 'max'])

    result4 = frame.apply(f)
    arr_info('result4', result4)
    print(result4)
    # Массив result4: <class 'pandas.core.frame.DataFrame'> 188661472 (2, 3)
    #             b         d         e
    # min -1.571244 -0.694143 -0.652199
    # max  1.877862  2.064941 -0.074198

    separator()

    # Также можно использовать поэлементные функции. Предположим, нужно
    # получить форматированную строку для каждого значения в объекте frame.
    # Это можно реализовать с помощью функции applymap:
    result5 = frame.applymap(lambda x: '%.2f' % x)
    arr_info('result5', result5)
    print(result5)
    # Массив result5: <class 'pandas.core.frame.DataFrame'> 188661520 (4, 3)
    #             b      d      e
    # Utah     1.88  -0.37  -0.45
    # Ohio    -0.32  -0.22  -0.65
    # Texas   -1.57  -0.69  -0.07
    # Oregon   1.67   2.06  -0.37

    separator()

    # В функции applymap используется метод map класса Series:
    result6 = frame['e'].map(lambda x: '%.2f' % x)
    arr_info('result6', result6)
    print(result6)
    # Массив result6: <class 'pandas.core.series.Series'> 188665184 (4,)
    # Utah      -0.45
    # Ohio      -0.65
    # Texas     -0.07
    # Oregon    -0.37
    # Name: e, dtype: object


if __name__ == '__main__':
    main()
