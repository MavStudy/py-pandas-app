# Pandas - структуры данных
#
# Series (ряд) — объект, типа одномерного массива, содержащий
# последовательность значений (типов, аналогичных типам NumPy)
# и связанный с ним массив меток данных, называемых индексами.
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
    # Создадим простейший объект Series только из массива данных:
    obj = pd.Series([4, 7, -5, 3])
    arr_info('obj', obj)
    # Массив obj: <class 'pandas.core.series.Series'> 42049440 (4,)
    print(obj)
    # 0    4
    # 1    7
    # 2   -5
    # 3    3
    # dtype: int64
    separator()

    # Строковое представление объекта Series в интерактивном режиме отображает
    # индексы слева, а данные справа. Так как мы не определили индексы, то
    # по умолчанию индексы содержат целыечислаот 0 до N‐1(где N—длина массива
    # данных).Можно получить представление в виде массива и индексы ряда
    # с помощью атрибутов values и index:
    print(obj.values)
    # [ 4  7 -5  3]

    separator()

    print(obj.index)
    # RangeIndex(start=0, stop=4, step=1)

    separator()

    # Частожелательносоздатьрядсиндексами,идентифицирующимикаждуюточкуданный
    # с меткой:
    obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
    arr_info('obj2', obj2)
    # Массив obj2: <class 'pandas.core.series.Series'> 42033504 (4,)
    print(obj2)
    # d    4
    # b    7
    # a   -5
    # c    3
    # dtype: int64

    separator()

    print(obj2.index)
    # Index(['d', 'b', 'a', 'c'], dtype='object')

    separator()

    # В отличие от массивов NumPy, можно использовать метки при индексации
    # при выборе отдельных значений или набора значений:
    print(obj2['a'])  # -5

    separator()

    obj2['d'] = 6

    separator()

    print(obj2[['c', 'a', 'd']])
    # c    3
    # a   -5
    # d    6
    # dtype: int64

    separator()

    # Использование функций NumPy или операций подобных NumPy, таких как
    # фильтраия с помощью булевых массивов, умножение на скаляр или вычисление
    # математических функций, сохраняет значения индексов:
    print("obj2[obj2 > 0]:")
    print(f"{obj2[obj2 > 0]}")
    # d    6
    # b    7
    # c    3
    # dtype: int64

    separator()

    print("obj2 * 2 =")
    print(f"{obj2 * 2}")
    # d    12
    # b    14
    # a   -10
    # c     6
    # dtype: int64

    separator()

    print("np.exp(obj2) =")
    print(np.exp(obj2))
    # d     403.428793
    # b    1096.633158
    # a       0.006738
    # c      20.085537
    # dtype: float64

    separator()

    # Series's (ряды) можно рассматривать как словари фиксированной длины:
    print(f"'b' in obj2 = {'b' in obj2}")
    # True

    print(f"'e' in obj2 = {'e' in obj2}")
    # False


if __name__ == '__main__':
    main()
