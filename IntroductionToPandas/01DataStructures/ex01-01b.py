# Pandas - структуры данных
#
# Series (ряд) — объект, типа одномерного массива, содержащий
# последовательность значений (типов, аналогичных типам NumPy)
# и связанный с ним массив меток данных, называемых индексами.
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
    # Series's (ряды) можно рассматривать как словари фиксированной длины.
    #
    # Если имеются данные, содержащиеся в словаре, можно создать ряд из него:
    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
    obj3 = pd.Series(sdata)
    arr_info('obj3', obj3)
    print(obj3)
    # Массив obj3: <class 'pandas.core.series.Series'> 41852832 (4,)
    # Ohio      35000
    # Texas     71000
    # Oregon    16000
    # Utah       5000
    # dtype: int64

    separator()

    # Если передается только словарь, то индексами ряда будут ключи словаря
    # в том порядке, в котором были при создании словаря. Можно изменить
    # порядок индекса передавая ключи словаря в порядке, который нужен:
    states = ['California', 'Ohio', 'Oregon', 'Texas']
    obj4 = pd.Series(sdata, index=states)
    arr_info('obj4', obj4)
    print(obj4)
    # Массив obj4: <class 'pandas.core.series.Series'> 188583696 (4,)
    # California        NaN
    # Ohio          35000.0
    # Oregon        16000.0
    # Texas         71000.0
    # dtype: float64

    # Здесь три значения, найденные в sdata, были размещены в соответствующих
    # местах, но так как не было найдено значение для ’California’, оно
    # отображается как NaN (не число), которое в pandas используется для
    # обозначения пропущенных значений или значений «NA» (not available).
    #
    # Поскольку ’Юта’ не была включена в states, этот элемент исключается из
    # результирующего объекта.

    separator()

    # Функции isnull и notnull в pandas используются для обнаружения
    # отсутствующих данных:
    print(pd.isnull(obj4))
    # California     True
    # Ohio          False
    # Oregon        False
    # Texas         False
    # dtype: bool

    separator()

    print(pd.notnull(obj4))
    # California    False
    # Ohio           True
    # Oregon         True
    # Texas          True
    # dtype: bool

    separator()

    # Класс Series также имеет эти методы:
    print(obj4.isnull())
    # California     True
    # Ohio          False
    # Oregon        False
    # Texas         False
    # dtype: bool

    separator()

    # Полезное свойство Series заключается в том, что она автоматически
    # происходит выравнивание по индексам в арифметических операциях:
    print(obj3)
    # Ohio      35000
    # Texas     71000
    # Oregon    16000
    # Utah       5000
    # dtype: int64

    separator()

    print(obj4)
    # California        NaN
    # Ohio          35000.0
    # Oregon        16000.0
    # Texas         71000.0
    # dtype: float64

    separator()

    print(obj3 + obj4)
    # California         NaN
    # Ohio           70000.0
    # Oregon         32000.0
    # Texas         142000.0
    # Utah               NaN
    # dtype: float64

    separator()

    # Как объекты Series, так и их индексы имеют атрибут name:
    print(f"{obj4.name = }")
    print(f"{obj4.index.name = }")

    separator()

    obj4.name = 'population'
    obj4.index.name = 'state'
    print(obj4)
    # state
    # California        NaN
    # Ohio          35000.0
    # Oregon        16000.0
    # Texas         71000.0
    # Name: population, dtype: float64

    separator()

    # Можно изменять индексы рядов присваиванием:
    obj = pd.Series([4, 7, -5, 3])
    arr_info('obj', obj)
    print(obj)
    # Массив obj: <class 'pandas.core.series.Series'> 188666544 (4,)
    # 0    4
    # 1    7
    # 2   -5
    # 3    3
    # dtype: int64

    obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
    arr_info('obj', obj)
    print(obj)
    # Массив obj: <class 'pandas.core.series.Series'> 188666544 (4,)
    # Bob      4
    # Steve    7
    # Jeff    -5
    # Ryan     3
    # dtype: int64


if __name__ == '__main__':
    main()
