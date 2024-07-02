# Pandas - Описательная и сводная статистика
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
    # Объекты pandas оснащены набором общих математических и статистических
    # методов.Большинство из них попадают в категорию сводной статистики.
    # В отличие от соответствующих методов массивов NumPy методы объектов
    # pandas имеют встроенную обработку пропущенных значений.

    # Рассмотрим небольшой объект DataFrame:
    df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                       [np.nan, np.nan], [0.75, -1.3]],
                      index=['a', 'b', 'c', 'd'],
                      columns=['one', 'two'])
    arr_info('df', df)
    print(df)
    # Массив df: <class 'pandas.core.frame.DataFrame'> 41983904 (4, 2)
    # one  two
    # a  1.40  NaN
    # b  7.10 -4.5
    # c   NaN  NaN
    # d  0.75 -1.3

    separator()

    # Вызов метода sum возвращает суммы значений по столбцам:
    print("Вызов метода sum возвращает суммы значений по столбцам:")
    print(df.sum())
    # Вызов метода sum возвращает суммы значений по столбцам:
    # one    9.25
    # two   -5.80
    # dtype: float64

    separator()

    # Чтобы получить суммы значений по строкам нужно передать параметр
    # axis=’columns’ или axis=1:
    print("Суммы значений по строкам:")
    print(df.sum(axis='columns'))
    # Суммы значений по строкам:
    # a    1.40
    # b    2.60
    # c    0.00
    # d   -0.55
    # dtype: float64

    separator()

    # Значения NaN исключаются, если только весь срез (в данном случае строка
    # или столбец) не равен NaN. Это поведение можно изменить с помощью
    # параметра skipna:
    print(r"df.mean(axis='columns', skipna=False):")
    print(df.mean(axis='columns', skipna=False))
    # a      NaN
    # b    1.300
    # c      NaN
    # d   -0.275
    # dtype: float64

    separator()

    # Некоторые методы,такие как idxmin и idxmax, возвращают косвенную
    # статистику, такую как значение индекса, где достигаются минимальные
    # или максимальные значения:
    print("df.idxmax():")
    print(df.idxmax())
    # df.idxmax():
    # one    b
    # two    d
    # dtype: object

    separator()

    # Есть методы являются аккумулирующими:
    print("df.cumsum():")
    print(df.cumsum())
    # df.cumsum():
    # one  two
    # a  1.40  NaN
    # b  8.50 -4.5
    # c   NaN  NaN
    # d  9.25 -5.8

    separator()

    # Метод describe возвращает множественную суммарную статистику:
    print("Метод describe возвращает множественную суммарную статистику:")
    print(df.describe())
    # Метод describe возвращает множественную суммарную статистику:
    # one       two
    # count  3.000000  2.000000
    # mean   3.083333 -2.900000
    # std    3.493685  2.262742
    # min    0.750000 -4.500000
    # 25%    1.075000 -3.700000
    # 50%    1.400000 -2.900000
    # 75%    4.250000 -2.100000
    # max    7.100000 -1.300000

    separator()

    # На нечисловых данных метод describe возвращает следующую информацию:
    obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
    arr_info('obj', obj)
    print(obj)
    # Массив obj: <class 'pandas.core.series.Series'> 39039280 (16,)
    # 0     a
    # 1     a
    # 2     b
    # 3     c
    # 4     a
    # 5     a
    # 6     b
    # 7     c
    # 8     a
    # 9     a
    # 10    b
    # 11    c
    # 12    a
    # 13    a
    # 14    b
    # 15    c
    # dtype: object

    separator()

    print("obj.describe():")
    print(obj.describe())
    # obj.describe():
    # count     16
    # unique     3
    # top        a
    # freq       8
    # dtype: object


if __name__ == '__main__':
    main()
#  Таблица 6: Описательная и сводная ститистика
# ----------------------------------------------------------------------------
#  Метод            |  Описание
# ----------------------------------------------------------------------------
#  count            |  Количество нечисловых значений
# ----------------------------------------------------------------------------
#  describe         |  Вычисляет сводную статистику для ряда или для каждого
#                   |  столбца объекта DataFrame
# ----------------------------------------------------------------------------
#  min, max         |  Вычисляет минимальное и максимальное значение
# ----------------------------------------------------------------------------
#  armin, argmax    |  Возвращают индекс (целое число), где расположено
#                   |  минимальное или максимальное значение
# ----------------------------------------------------------------------------
#  inxmin, idxmax   |  Возвращают метку индекса, где расположено минимальное
#                   |  или максимальное значение
# ----------------------------------------------------------------------------
#  quantile         |  Вычиляет квантиль выборки от 0 до 1
# ----------------------------------------------------------------------------
#  sum              |  Сумма значений
# ----------------------------------------------------------------------------
#  mean             |  Среднее значение
# ----------------------------------------------------------------------------
#  median           |  Медиана (50-процентная квантиль) значений
# ----------------------------------------------------------------------------
#  mad              |  Среднее абсолютное отклонение от среднего значения
# ----------------------------------------------------------------------------
#  prod             |  Произведение значений
# ----------------------------------------------------------------------------
#  var              |  Дисперсия множества выборки значений
# ----------------------------------------------------------------------------
#  std              |  Стандартное октлонение выборки значений
# ----------------------------------------------------------------------------
#  skew             |  Асимметрия (третий момент) выборки значений
# ----------------------------------------------------------------------------
#  kurt             |  Эксцесс (четвёртый момент) выборки значений
# ----------------------------------------------------------------------------
#  cumsum           |  Накопленная сумма значений
# ----------------------------------------------------------------------------
#  cummin, cummax   |  Совокупный минимум и максимум
# ----------------------------------------------------------------------------
#  cumprod          |  Накопленное произведение значений
# ----------------------------------------------------------------------------
#  diff             |  Вычисляет первую арифметическую разность (полезно
#                   |  для временных рядов)
# ----------------------------------------------------------------------------
#  pct_change       |  Вычисляет процентные изменения
# ----------------------------------------------------------------------------