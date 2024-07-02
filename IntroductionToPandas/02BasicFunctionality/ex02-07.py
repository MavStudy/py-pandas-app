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
    #  Индексация с повторяющимися метками
    #
    # В рассматриваемых выше примерах индексы имели единственные значения,
    # без повторений.
    # Хотя многие функции библиотеки pandas (например, reindex) требуют, чтобы
    # метки были уникальными, это не обязательно.

    # Рассмотрим ряд с повторяющимися индексами:
    obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
    arr_info('obj', obj)
    print(obj)
    # Массив obj: <class 'pandas.core.series.Series'> 31568176 (5,)
    # a    0
    # a    1
    # b    2
    # b    3
    # c    4
    # dtype: int64

    separator()

    # У объекта Index есть атрибут is_unique, который дает информацию являются
    # ли метки индекса уникальными:
    print(f"{obj.index.is_unique = }")
    # obj.index.is_unique = False

    separator()

    # Вслучае,когда несколько данных имеют одинаковые метки, обращение по этому
    # индексу вернёт объект Series, в то время как для меток без дублирования
    # возвращается скалярное значение:
    result1 = obj['a']
    arr_info('result1', result1)
    print(result1)
    # Массив result1: <class 'pandas.core.series.Series'> 188666592 (2,)
    # a    0
    # a    1
    # dtype: int64

    separator()

    result2 = obj['c']
    print(f"{type(result2) = }, {result2 = }")
    # type(result2) = <class 'numpy.int64'>, result2 = 4

    separator()

    # Та же логика распространяется и на индексирование строк в DataFrame:
    df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
    arr_info('df', df)
    print(df)
    # Массив df: <class 'pandas.core.frame.DataFrame'> 38909648 (4, 3)
    #           0         1         2
    # a  0.989071 -0.393497  0.132760
    # a  0.349078 -0.790946 -0.668568
    # b -1.336198 -1.964827 -1.018762
    # b  0.937514 -0.570278 -2.021959

    separator()

    result3 = df.loc['b']
    arr_info('result3', result3)
    print(result3)
    # Массив result3: <class 'pandas.core.frame.DataFrame'> 188667552 (2, 3)
    # 0         1         2
    # b  2.345598  1.139426  0.115341
    # b  0.475449 -0.239212 -0.475019


if __name__ == '__main__':
    main()
