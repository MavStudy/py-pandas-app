# Pandas - структуры данных
#
# Объекты типа Index в pandas отвечают за хранение меток осей и других
# метаданных (таких как имя или имя оси).
import numpy as np
import pandas as pd


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
    # Любой массив или другая последовательность меток, которые используются
    # при создании Series или DataFrame, преобразуется в Index:
    obj = pd.Series(range(3), index=['a', 'b', 'c'])
    index = obj.index
    arr_info('index', index)
    print(index)
    # Массив index: <class 'pandas.core.indexes.base.Index'> 30716208 (3,)
    # Index(['a', 'b', 'c'], dtype='object')

    separator()

    print("index[1:]:", end=' ')
    print(index[1:])

    separator()

    # Объекты Index — неизменяемый тип и не может изменяться пользователем !!!
    #
    # index[1] = 'd'
    #
    # raise TypeError("Index does not support mutable operations")
    # TypeError: Index does not support mutable operations

    # Неизменяемость делает более безопасным совместное использование
    # объектов Index:
    labels = pd.Index(np.arange(3))
    arr_info('labels', labels)
    print(labels)
    # Массив labels: <class 'pandas.core.indexes.base.Index'> 42677872 (3,)
    # Index([0, 1, 2], dtype='int32')

    separator()

    obj2 = pd.Series([1.5, -2.5, 0], index=labels)
    arr_info('obj2', obj2)
    print(obj2)
    # Массив obj2: <class 'pandas.core.series.Series'> 188728032 (3,)
    # 0    1.5
    # 1   -2.5
    # 2    0.0
    # dtype: float64

    separator()

    print("obj2.index is labels: ", f"{obj2.index is labels}")
    # obj2.index is labels:  True

    separator()

    # Если вложенный словарь передать в конструктор DataFrame, pandas
    # интерпретируетключи внешнего словаря как столбцы, а внутренние ключи —
    # как индексы:
    pop = {'Nevada': {2001: 2.4, 2002: 2.9},
           'Ohio': {2001: 1.7, 2002: 3.6, 2000: 1.5},
           }
    frame3 = pd.DataFrame(pop)
    # arr_info('frame3', frame3)
    # Если для индекса и столбцов DataFrame установлены атрибуты name,
    # они также будут отображены:
    frame3.index.name = 'year'
    frame3.columns.name = 'state'

    # С объектами Index можно работать как с массивами фиксированного размера:
    arr_info('frame3', frame3)
    print(frame3)
    # Массив frame3: <class 'pandas.core.frame.DataFrame'> 188728176 (3, 2)
    # state  Nevada  Ohio
    # year
    # 2001      2.4   1.7
    # 2002      2.9   3.6
    # 2000      NaN   1.5

    separator()

    print(frame3.columns)
    # Index(['Nevada', 'Ohio'], dtype='object', name='state')

    separator()

    print("'Ohio' in frame3.columns:", end=' ')
    print('Ohio' in frame3.columns)

    separator()

    print("2003 in frame3.index:", end=' ')
    print(2003 in frame3.index)

    separator()

    # В отличие от множеств Python объекты Index могут содержать
    # повторяющиеся метки:
    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
    obj3 = pd.Series(sdata)
    arr_info('obj3', obj3)
    print(obj3)

    separator()


if __name__ == '__main__':
    main()

# Таблица 2: Некоторые методы и свойства Index

# ----------------------------------------------------------------------------
# Метод             | Описание
# ----------------------------------------------------------------------------
# append            | Добавляет дополнительные объекты Index, создавая
#                   | новый объект Index
# ----------------------------------------------------------------------------
# difference        | Возвращает разность множеств как Index
# ----------------------------------------------------------------------------
# intersection      | Возвращает пересечение множеств
# ----------------------------------------------------------------------------
# union             | Возвращает объединение множеств
# ----------------------------------------------------------------------------
# isin              | Возвращает логический массив, указывающий, содержится ли
#                   | каждое значение в переданной коллекции
# ----------------------------------------------------------------------------
# delete            | Возвращает новый объект Index с удалённым элементом
#                   | по индексу i
# ----------------------------------------------------------------------------
# drop              | Возвращает новый объект Index, удаляя переданные
#                   | значения
# ----------------------------------------------------------------------------
# insert            | Возвращает новый объект Index, вставляя по индексу i
#                   | элемент
# ----------------------------------------------------------------------------
# is_monotonic      | Возвращает True, если каждый элемент больше предыдущего
#                   | либо равен ему
# ----------------------------------------------------------------------------
# is_unique         | Возвращает True, если объект Index не содержит
#                   | дубликатов
# ----------------------------------------------------------------------------
# unique            | Возвращает массив уникальных значений в объекте Index
# ----------------------------------------------------------------------------
