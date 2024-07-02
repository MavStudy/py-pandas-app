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
    #  Сортировка и ранжирование
    #
    # Одна из важных встроенных операций — это сортировка данных. Для того,
    # чтобы выполнить лексикографическую сортировку по индексам строк или
    # столбцов, можно использовать функцию sort_index, которая возвращает
    # новый отсортированный объект:
    obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
    arr_info('obj', obj)
    print(obj)
    # Массив obj: <class 'pandas.core.series.Series'> 4372176 (4,)
    # d    0
    # a    1
    # b    2
    # c    3
    # dtype: int64

    separator()

    obj = obj.sort_index()
    arr_info('obj', obj)
    print(obj)
    # Массив obj: <class 'pandas.core.series.Series'> 188658400 (4,)
    # a    1
    # b    2
    # c    3
    # d    0
    # dtype: int64

    separator()

    # Объект DataFrame можно сортировать по индексам на любой оси:
    frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                         index=['three', 'one'],
                         columns=['d', 'a', 'b', 'c'])
    arr_info('frame', frame)
    print(frame)
    # Массив frame: <class 'pandas.core.frame.DataFrame'> 186318704 (2, 4)
    #        d  a  b  c
    # three  0  1  2  3
    # one    4  5  6  7

    separator()

    frame1 = frame.sort_index()
    arr_info('frame1', frame1)
    print(frame1)
    # Массив frame1: <class 'pandas.core.frame.DataFrame'> 188658976 (2, 4)
    #        d  a  b  c
    # one    4  5  6  7
    # three  0  1  2  3

    separator()

    frame2 = frame.sort_index(axis=1)
    arr_info('frame2', frame2)
    print(frame2)
    # Массив frame2: <class 'pandas.core.frame.DataFrame'> 188659024 (2, 4)
    #        a  b  c  d
    # three  1  2  3  0
    # one    5  6  7  4

    separator()

    # Данные сортируются по возрастанию по умолчанию, но могут быть
    # отсортированы также по убыванию:
    frame3 = frame.sort_index(axis=1, ascending=False)
    arr_info('frame3', frame3)
    print(frame3)
    # Массив frame3: <class 'pandas.core.frame.DataFrame'> 188658928 (2, 4)
    #        d  c  b  a
    # three  0  3  2  1
    # one    4  7  6  5

    separator()

    # Для сортировки объекта Series по значениям
    # используется метод sort_values:
    obj = pd.Series([4, 7, -3, 2])
    obj = obj.sort_values()
    arr_info('obj', obj)
    print(obj)
    # Массив obj: <class 'pandas.core.series.Series'> 39106256 (4,)
    # 2   -3
    # 3    2
    # 0    4
    # 1    7
    # dtype: int64

    separator()

    # Все пропущенные значения по умолчанию сортируются в конец объекта Series:
    obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
    obj = obj.sort_values()
    arr_info('obj', obj)
    print(obj)
    # Массив obj: <class 'pandas.core.series.Series'> 31700688 (6,)
    # 4   -3.0
    # 5    2.0
    # 0    4.0
    # 2    7.0
    # 1    NaN
    # 3    NaN
    # dtype: float64

    separator()

    # При сортировке объекта DataFrame можно использовать данные в одном или
    # нескольких столбцах в качестве ключей для сортировки. Чтобы выполнить
    # это, необходимо передать имя одного или нескольких столбцов параметру
    # by метода sort_vlues
    frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
    arr_info('frame', frame)
    print(frame)
    # Массив frame: <class 'pandas.core.frame.DataFrame'> 188661088 (4, 2)
    # b  a
    # 0  4  0
    # 1  7  1
    # 2 -3  0
    # 3  2  1

    separator()

    frame1 = frame.sort_values(by='b')
    arr_info('frame1', frame1)
    print(frame1)
    # Массив frame1: <class 'pandas.core.frame.DataFrame'> 188661040 (4, 2)
    # b  a
    # 2 -3  0
    # 3  2  1
    # 0  4  0
    # 1  7  1

    separator()

    # Для сортировки по нескольким столбцам, необходимо передать
    # список имён столбцов:
    frame2 = frame.sort_values(by=['a', 'b'])
    arr_info('frame2', frame2)
    print(frame2)
    # Массив frame2: <class 'pandas.core.frame.DataFrame'> 188660368 (4, 2)
    # b  a
    # 2 -3  0
    # 0  4  0
    # 3  2  1
    # 1  7  1

    separator()

    # ************************************************************************
    # Ранжирование заключается в присвоении ранга от единицы до числа значений
    # в массиве.
    # ************************************************************************

    # Объекты Series и DataFrame имеют метод rank, который по
    # умолчанию разрывает связи, присваивая каждой группе среднее значение
    # ранга:
    obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
    arr_info('obj', obj)
    print(obj)

    separator()

    rank1 = obj.rank()
    arr_info('rank1', rank1)
    print(rank1)
    # Массив rank1: <class 'pandas.core.series.Series'> 188664848 (7,)
    # 0    6.5
    # 1    1.0
    # 2    6.5
    # 3    4.5
    # 4    3.0
    # 5    2.0
    # 6    4.5
    # dtype: float64

    separator()

    rank2 = obj.rank(method='first')
    arr_info('rank2', rank2)
    print(rank2)
    # Массив rank2: <class 'pandas.core.series.Series'> 188881216 (7,)
    # 0    6.0
    # 1    1.0
    # 2    7.0
    # 3    4.0
    # 4    3.0
    # 5    2.0
    # 6    5.0
    # dtype: float64

    # Здесь вместо использования среднего ранга 6.5 для записей с индексами 0
    # и 2 они вместо этого были установлены на 6 и 7, потому что метка 0
    # предшествует метке 2 в данных.

    # В таблице 5 представлен перечень методов построения ранга.

    separator()

    # Объект DataFrame может вычислять ранги по строкам или по столбцам:
    frame = pd.DataFrame({'b': [4.3, 7, -3, 2],
                          'a': [0, 1, 0, 1],
                          'c': [-2, 5, 8, -2.5]})
    arr_info('frame', frame)
    print(frame)
    # Массив frame: <class 'pandas.core.frame.DataFrame'> 188587936 (4, 3)
    # b  a    c
    # 0  4.3  0 -2.0
    # 1  7.0  1  5.0
    # 2 -3.0  0  8.0
    # 3  2.0  1 -2.5

    separator()

    rank3 = frame.rank(axis='columns')
    arr_info('rank3', rank3)
    print(rank3)
    # Массив rank3: <class 'pandas.core.frame.DataFrame'> 188663168 (4, 3)
    # b    a    c
    # 0  3.0  2.0  1.0
    # 1  3.0  1.0  2.0
    # 2  1.0  2.0  3.0
    # 3  3.0  2.0  1.0

    separator()


if __name__ == '__main__':
    main()
#  Таблица 5: Методы ранжирования
# ----------------------------------------------------------------------------
#  Метод        |  Описание
# ----------------------------------------------------------------------------
#  average      |  Используется по умолчанию. Присваивает среднее значение
#               |  рангра каждому значению в группе
# ----------------------------------------------------------------------------
#  min          |  Использует минимальный ранг для всей группы
# ----------------------------------------------------------------------------
#  max          |  Использует максимальный ранг для всей группы
# ----------------------------------------------------------------------------
#  first        |  Присваивает ранги в порядке появления значений в данных
# ----------------------------------------------------------------------------
#  dense        |  Как method = 'min', но ранги между группами всегда
#               |  увеличиваются на 1, а не на количество раных элементов
#               |  в группе
# ----------------------------------------------------------------------------
