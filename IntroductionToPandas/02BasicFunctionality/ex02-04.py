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
    # Операции между объектами DataFrame и Series
    #
    # Как и для массивов NumPy разной размерности, существуют арифметические
    # операции между объектами DataFrame и Series.

    # В качестве примера рассмотрим разность между двумерным массивом и одной
    # из его строк:
    arr = np.arange(12.).reshape((3, 4))
    arr_info('arr', arr)
    print(arr)
    # Массив arr: <class 'numpy.ndarray'> 188550672 (3, 4)
    # [[ 0.  1.  2.  3.]
    #  [ 4.  5.  6.  7.]
    #  [ 8.  9. 10. 11.]]

    separator()

    print(f"{arr[0] = }")

    separator()

    result1 = arr - arr[0]
    arr_info('result1', result1)
    print(result1)
    # Массив result1: <class 'numpy.ndarray'> 188686384 (3, 4)
    # [[0. 0. 0. 0.]
    #  [4. 4. 4. 4.]
    #  [8. 8. 8. 8.]]

    # При вычитании arr[0] из arr, операция осуществляется для каждой строки.
    # Операции между DataFrame и Series производятся аналогично.

    separator()

    frame = pd.DataFrame(np.arange(12.).reshape(4, 3),
                         columns=list('bde'),
                         index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    arr_info('frame', frame)
    print(frame)
    # Массив frame: <class 'pandas.core.frame.DataFrame'> 42082800 (4, 3)
    #           b     d     e
    # Utah    0.0   1.0   2.0
    # Ohio    3.0   4.0   5.0
    # Texas   6.0   7.0   8.0
    # Oregon  9.0  10.0  11.0

    separator()

    series = frame.iloc[0]
    arr_info('series', series)
    print(series)
    # Массив series: <class 'pandas.core.series.Series'> 188666448 (3,)
    # b    0.0
    # d    1.0
    # e    2.0
    # Name: Utah, dtype: float64

    separator()

    # По умолчанию арифметические операции между DataFrame и Series приводят
    # индексы объекта Series к столбцам объекта DataFrame, распространяя
    # операцию по строкам:
    result2 = frame - series
    arr_info('result2', result2)
    print(result2)
    # Массив result2: <class 'pandas.core.frame.DataFrame'> 42482272 (4, 3)
    #           b    d    e
    # Utah    0.0  0.0  0.0
    # Ohio    3.0  3.0  3.0
    # Texas   6.0  6.0  6.0
    # Oregon  9.0  9.0  9.0

    separator()

    # Если значение индекса не найдено ни встолбцах DataFrame, ни в индексе
    # Series, объекты будут переиндексированы для формирования объединения:
    series2 = pd.Series(range(3), index=['b', 'e', 'f'])
    arr_info('series2', series2)
    print(series2)
    # Массив series2: <class 'pandas.core.series.Series'> 188669184 (3,)
    # b    0
    # e    1
    # f    2
    # dtype: int64

    separator()

    result3 = frame + series2
    arr_info('result3', result3)
    print(result3)
    # Массив result3: <class 'pandas.core.frame.DataFrame'> 188663840 (4, 4)
    #           b   d     e   f
    # Utah    0.0 NaN   3.0 NaN
    # Ohio    3.0 NaN   6.0 NaN
    # Texas   6.0 NaN   9.0 NaN
    # Oregon  9.0 NaN  12.0 NaN

    separator()

    arr_info('frame', frame)
    print(frame)
    # Массив frame: <class 'pandas.core.frame.DataFrame'> 42410480 (4, 3)
    # b     d     e
    # Utah    0.0   1.0   2.0
    # Ohio    3.0   4.0   5.0
    # Texas   6.0   7.0   8.0
    # Oregon  9.0  10.0  11.0

    separator()

    # Если вместо согласования по столбцам нужно согласовывать операцию
    # по строкам, нужно использовать арифметический метод:
    series3 = frame['d']
    arr_info('series3', series3)
    print(series3)
    # Массив series3: <class 'pandas.core.series.Series'> 188665712 (4,)
    # Utah       1.0
    # Ohio       4.0
    # Texas      7.0
    # Oregon    10.0
    # Name: d, dtype: float64

    separator()

    result4 = frame.sub(series3, axis='index')
    arr_info('result4', result4)
    print(result4)

    separator()


if __name__ == '__main__':
    main()
