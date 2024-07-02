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
    # Удаление записей с оси
    #
    # Удалить одну или несколько записей легко, если имеется массив или список
    # индексов, которые не содержат эти записи. Поскольку это может потребовать
    # некоторых операций над множествами,метод drop возвращает новый объект
    # с указанными значениями, удаленнымис оси:

    # Рассмотрим пример:
    obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
    arr_info('obj', obj)
    print(obj)
    # Массив obj: <class 'pandas.core.series.Series'> 30717648 (5,)
    # a    0.0
    # b    1.0
    # c    2.0
    # d    3.0
    # e    4.0
    # dtype: float64

    separator()

    new_obj = obj.drop('c')
    arr_info('new_obj', new_obj)
    print(new_obj)
    # Массив new_obj: <class 'pandas.core.series.Series'> 188662352 (4,)
    # a    0.0
    # b    1.0
    # d    3.0
    # e    4.0
    # dtype: float64

    separator()

    new_obj2 = obj.drop(['d', 'c'])
    arr_info('new_obj2', new_obj2)
    print(new_obj2)
    # Массив new_obj2: <class 'pandas.core.series.Series'> 188666832 (3,)
    # a    0.0
    # b    1.0
    # e    4.0
    # dtype: float64

    separator()

    # В DataFrame значения индекса могут быть удалены с любой оси:
    data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                        index=['Ohio', 'Colorado', 'Utah', 'New Your'],
                        columns=['one', 'two', 'three', 'four'])
    arr_info('data', data)
    print(data)
    # Массив data: <class 'pandas.core.frame.DataFrame'> 188667408 (4, 4)
    # one  two  three  four
    # Ohio        0    1      2     3
    # Colorado    4    5      6     7
    # Utah        8    9     10    11
    # New Your   12   13     14    15

    separator()

    # Вызов drop с последовательностью меток
    # удаляет значения из меток строк (ось 0):
    data1 = data.drop(['Colorado', 'Ohio'])
    arr_info('data1', data1)
    print(data1)
    # Массив data1: <class 'pandas.core.frame.DataFrame'> 188667120 (2, 4)
    # one  two  three  four
    # Utah        8    9     10    11
    # New Your   12   13     14    15

    separator()

    # Удалить значения в столбцах можно
    # передавая параметр axis=1 или axis=columns:
    data2 = data.drop('two', axis=1)
    arr_info('data2', data2)
    print(data2)
    # Массив data2: <class 'pandas.core.frame.DataFrame'> 188659408 (4, 3)
    # one  three  four
    # Ohio        0      2     3
    # Colorado    4      6     7
    # Utah        8     10    11
    # New Your   12     14    15

    separator()

    data3 = data.drop(['two', 'four'], axis='columns')
    arr_info('data3', data3)
    print(data3)
    # Массив data3: <class 'pandas.core.frame.DataFrame'> 188859776 (4, 2)
    # one  three
    # Ohio        0      2
    # Colorado    4      6
    # Utah        8     10
    # New Your   12     14

    separator()

    # Многие функции,такие как drop,которые изменяют размер или форму Series
    # или DataFrame, могут изменять сам объект (in‑place) без создания нового
    # объекта:
    arr_info('obj', obj)
    print(obj)
    # Массив obj: <class 'pandas.core.series.Series'> 30717648 (5,)
    # a    0.0
    # b    1.0
    # c    2.0
    # d    3.0
    # e    4.0
    # dtype: float64

    separator()

    obj.drop('c', inplace=True)
    arr_info('obj', obj)
    print(obj)
    # Массив obj: <class 'pandas.core.series.Series'> 30717648 (4,)
    # a    0.0
    # b    1.0
    # d    3.0
    # e    4.0
    # dtype: float64

    separator()

    # Предупреждение !!!
    #
    # Будьте осторожны с параметром inplace,
    # так как происходит удаление данных!


if __name__ == '__main__':
    main()
