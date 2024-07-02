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
    # Арифметические операции и выравнивание данных
    #
    # Важной особенностью pandas для некоторых приложений является поведение
    # арифметических операций между объектами с разными индексами. При сложении
    # объекты в случае,когда любые пары индексов отличаются, соответствующий
    # индекс в результате является объединением исходных индексов:
    s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
    arr_info('s1', s1)
    print(s1)
    # Массив s1: <class 'pandas.core.series.Series'> 41918368 (4,)
    # a    7.3
    # c   -2.5
    # d    3.4
    # e    1.5
    # dtype: float64

    separator()

    s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
    arr_info('s2', s2)
    print(s2)
    # Массив s2: <class 'pandas.core.series.Series'> 188662016 (5,)
    # a   -2.1
    # c    3.6
    # e   -1.5
    # f    4.0
    # g    3.1
    # dtype: float64

    separator()

    result1 = s1 + s2
    arr_info('result1', result1)
    print(result1)
    # Массив result1: <class 'pandas.core.series.Series'> 41902384 (6,)
    # a    5.2
    # c    1.1
    # d    NaN
    # e    0.0
    # f    NaN
    # g    NaN
    # dtype: float64

    separator()

    # Выравнивание данных вводит пропущенные значения в местах меток, которые
    # не пересекаются. Пропущенные значения будут распространяться в дальнейших
    # арифметических вычислениях.

    # В случае DataFrame выравнивание осуществляется как для строк,
    # так и для столбцов:
    df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)),
                       columns=list('bcd'),
                       index=['Ohio', 'Texas', 'Colorado'])
    arr_info('df1', df1)
    print(df1)
    # Массив df1: <class 'pandas.core.frame.DataFrame'> 188667168 (3, 3)
    # b    c    d
    # Ohio      0.0  1.0  2.0
    # Texas     3.0  4.0  5.0
    # Colorado  6.0  7.0  8.0

    separator()

    df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                       columns=list('bde'),
                       index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    arr_info('df2', df2)
    print(df2)
    # Массив df2: <class 'pandas.core.frame.DataFrame'> 188667552 (4, 3)
    # b     d     e
    # Utah    0.0   1.0   2.0
    # Ohio    3.0   4.0   5.0
    # Texas   6.0   7.0   8.0
    # Oregon  9.0  10.0  11.0

    separator()

    # Сумма введенных объектов вернет новый объект DataFrame, чьи индексы
    # и столбцы являются объединениями индексов и столбцов двух складываемых
    # объектов:
    result2 = df1 + df2
    arr_info('result2', result2)
    print(result2)
    # Массив result2: <class 'pandas.core.frame.DataFrame'> 188868208 (5, 4)
    # b   c     d   e
    # Colorado  NaN NaN   NaN NaN
    # Ohio      3.0 NaN   6.0 NaN
    # Oregon    NaN NaN   NaN NaN
    # Texas     9.0 NaN  12.0 NaN
    # Utah      NaN NaN   NaN NaN

    # Так как столбцы ’c’ и ’e’ не находятся одновременно в обоих объектах
    # DataFrame, в результате они содержат отсутствующие значения. Такое же
    # происходит и со строками.

    separator()

    # Если сложить объекты DataFrame без общих меток столбцов или строк,
    # результат будет содержать все отсутствующие значения:
    df1 = pd.DataFrame({'A': [1, 2]})
    arr_info('df1', df1)
    print(df1)
    # Массив df1: <class 'pandas.core.frame.DataFrame'> 188667984 (2, 1)
    # A
    # 0  1
    # 1  2

    separator()

    df2 = pd.DataFrame({'B': [3, 4]})
    arr_info('df2', df2)
    print(df2)
    # Массив df2: <class 'pandas.core.frame.DataFrame'> 188667168 (2, 1)
    # B
    # 0  3
    # 1  4

    separator()

    result3 = df1 - df2
    arr_info('result3', result3)
    print(result3)
    # Массив result3: <class 'pandas.core.frame.DataFrame'> 188672176 (2, 2)
    # A   B
    # 0 NaN NaN
    # 1 NaN NaN

    separator()

    # ************************************************
    #  Арифметические методы с заполнением значений. *
    # ************************************************
    df1 = pd.DataFrame(np.arange(12.).reshape(3, 4),
                       columns=list('abcd'))
    arr_info('df1', df1)
    print(df1)
    # Массив df1: <class 'pandas.core.frame.DataFrame'> 188661712 (3, 4)
    #      a    b     c     d
    # 0  0.0  1.0   2.0   3.0
    # 1  4.0  5.0   6.0   7.0
    # 2  8.0  9.0  10.0  11.0

    separator()

    df2 = pd.DataFrame(np.arange(20.).reshape(4, 5),
                       columns=list('abcde'))
    df2.loc[1, 'b'] = np.nan
    arr_info('df2', df2)
    print(df2)
    # Массив df2: <class 'pandas.core.frame.DataFrame'> 188665616 (4, 5)
    # a     b     c     d     e
    # 0   0.0   1.0   2.0   3.0   4.0
    # 1   5.0   NaN   7.0   8.0   9.0
    # 2  10.0  11.0  12.0  13.0  14.0
    # 3  15.0  16.0  17.0  18.0  19.0

    separator()

    # Сложение этих объектов приводит к значениям NaN в местах,
    # которые не перекрываются:
    result4 = df1 + df2
    arr_info('result4', result4)
    print(result4)
    # Массив result4: <class 'pandas.core.frame.DataFrame'> 188989888 (4, 5)
    # a     b     c     d   e
    # 0   0.0   2.0   4.0   6.0 NaN
    # 1   9.0   NaN  13.0  15.0 NaN
    # 2  18.0  20.0  22.0  24.0 NaN
    # 3   NaN   NaN   NaN   NaN NaN

    separator()

    # Для заполнения отсутствующих значений можно воспользоваться функцией add
    # с дополнительным аргументом fill_value:
    result5 = df1.add(df2, fill_value=0)
    arr_info('result5', result5)
    print(result5)
    # Массив result5: <class 'pandas.core.frame.DataFrame'> 188669616 (4, 5)
    # a     b     c     d     e
    # 0   0.0   2.0   4.0   6.0   4.0
    # 1   9.0   5.0  13.0  15.0   9.0
    # 2  18.0  20.0  22.0  24.0  14.0
    # 3  15.0  16.0  17.0  18.0  19.0

    separator()

    # В таблице 4 представлены методы для арифметических операций. У каждого
    # из них есть аналог, начинающийся с буквы r, у которого переставлены
    # аргументы.

    # Приведённые ниже примеры эквивалентны:
    example1 = 1 / df1
    arr_info('example1', example1)
    print(example1)
    # Массив example1: <class 'pandas.core.frame.DataFrame'> 188665472 (3, 4)
    # a         b         c         d
    # 0    inf  1.000000  0.500000  0.333333
    # 1  0.250  0.200000  0.166667  0.142857
    # 2  0.125  0.111111  0.100000  0.090909

    separator()

    example2 = df1.rdiv(1)
    arr_info('example2', example2)
    print(example2)
    # Массив example2: <class 'pandas.core.frame.DataFrame'> 188900064 (3, 4)
    # a         b         c         d
    # 0    inf  1.000000  0.500000  0.333333
    # 1  0.250  0.200000  0.166667  0.142857
    # 2  0.125  0.111111  0.100000  0.090909

    separator()

    # Соответственно, при переиндексации Series или DataFrame вы также можете
    # указать другое значение заполнения:
    arr_info('df1', df1)
    print(df1)
    # Массив df1: <class 'pandas.core.frame.DataFrame'> 188665760 (3, 4)
    # a    b     c     d
    # 0  0.0  1.0   2.0   3.0
    # 1  4.0  5.0   6.0   7.0
    # 2  8.0  9.0  10.0  11.0

    separator()

    df1 = df1.reindex(columns=df2.columns, fill_value=0)
    arr_info('df1', df1)
    print(df1)
    # Массив df1: <class 'pandas.core.frame.DataFrame'> 188991712 (3, 5)
    # a    b     c     d  e
    # 0  0.0  1.0   2.0   3.0  0
    # 1  4.0  5.0   6.0   7.0  0
    # 2  8.0  9.0  10.0  11.0  0


if __name__ == '__main__':
    main()
#   Таблица 4: Гибкие арифметические методы
# ---------------------------------------------------------------------------
#  Метод        |  Описание
# ---------------------------------------------------------------------------
#  add, radd    |  Сложение (+)
# ---------------------------------------------------------------------------
#  sub, rsub    |  Вычитание (-)
# ---------------------------------------------------------------------------
#  div, rdiv    |  Деление (/)
# ---------------------------------------------------------------------------
#  floordiv,    |  Целочисленное деление (//)
#  rfloordiv    |
# ---------------------------------------------------------------------------
#  mul, rmul    |  Умножение (*)
# ---------------------------------------------------------------------------
#  pow, rpow    |  Возведение в степень (**)
# ---------------------------------------------------------------------------
