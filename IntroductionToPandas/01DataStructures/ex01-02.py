# Pandas - структуры данных
#
# DataFrame представляет собой прямоугольную таблицу данных и содержит
# упорядоченную коллекцию столбцов, каждый из которых может иметь различный
# тип значения (числовой, строковый, логический и т.д.).
# DataFrame имеет индексы столбцов и строк.
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
    # Есть много способов создания объекта DataFrame, хотя один из наиболее
    # распространённых - это ипользование списков, словарей или массивов NumPy:
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
            }

    frame = pd.DataFrame(data)
    # Полученный в результате DataFrame получит автоматически индексацию для
    # строк (как в Series), а индексом столбцов будут ключи словаря.

    arr_info('frame', frame)
    print(frame)
    #     state  year  pop
    # 0    Ohio  2000  1.5
    # 1    Ohio  2001  1.7
    # 2    Ohio  2002  3.6
    # 3  Nevada  2001  2.4
    # 4  Nevada  2002  2.9
    # 5  Nevada  2003  3.2

    # Если используется блокнот Jupyter, объекты DataFrame будут отображаться
    # в виде более  удобной для просмотра HTML‑таблицы.

    separator()

    # Для больших DataFrames метод head выбирает только первые пять строк:
    print("frame.head():")
    print(frame.head())

    separator()

    # Можно задавать другой порядок столбцов:
    print(pd.DataFrame(data, columns=['year', 'state', 'pop']))
    #    year   state  pop
    # 0  2000    Ohio  1.5
    # 1  2001    Ohio  1.7
    # 2  2002    Ohio  3.6
    # 3  2001  Nevada  2.4
    # 4  2002  Nevada  2.9
    # 5  2003  Nevada  3.2

    separator()

    # Если передать столбец, который не содержится в словаре, то в результате
    # будет столбец с отсутствующими значениями:
    frame2 = pd.DataFrame(
        data,
        columns=['year', 'state', 'pop', 'debt'],
        index=['one', 'two', 'three', 'four', 'five', 'six']
    )
    arr_info('frame2', frame2)
    print(frame2)

    separator()

    print(frame2.columns)
    # Index(['year', 'state', 'pop', 'debt'], dtype='object')

    separator()

    # К столбцу DataFrame можно получить доступ как к ряду с помощью нотацией
    # подобной словарю или через атрибут:
    print("frame2['state']:")
    print(frame2['state'])
    # frame2['state']:
    # one        Ohio
    # two        Ohio
    # three      Ohio
    # four     Nevada
    # five     Nevada
    # six      Nevada
    # Name: state, dtype: object

    separator()

    print("frame2.year:")
    print(frame2.year)
    # frame2.year:
    # one      2000
    # two      2001
    # three    2002
    # four     2001
    # five     2002
    # six      2003
    # Name: year, dtype: int64

    # Замечание
    #
    # IPython предоставлет доступ по атрибуту (например, frame2.year)
    # по автодополнению с помощью клавиши <TAB>.

    # Вариант frame2[column] работает для любых имен столбцов, в то время как
    # frame2.column работает толькое если имя столбца является допустимым
    # в Python именем переменной.

    separator()

    # К строкам можно получить доступ по позиции или с помощью специального
    # атрибута loc:
    print("frame2.loc['tree']:")
    print(frame2.loc['three'])
    # frame2.loc['tree']:
    # year     2002
    # state    Ohio
    # pop       3.6
    # debt      NaN
    # Name: three, dtype: object

    separator()

    # Можно менять значения столбцов. Например, пустой столбцу debt можно
    # присвоить скалярное значение или массив:
    frame2['debt'] = 16.5
    arr_info('frame2', frame2)
    print(frame2)
    # Массив frame2: <class 'pandas.core.frame.DataFrame'> 42285712 (6, 4)
    # year   state  pop  debt
    # one    2000    Ohio  1.5  16.5
    # two    2001    Ohio  1.7  16.5
    # three  2002    Ohio  3.6  16.5
    # four   2001  Nevada  2.4  16.5
    # five   2002  Nevada  2.9  16.5
    # six    2003  Nevada  3.2  16.5

    separator()

    frame2['debt'] = np.arange(6.)
    arr_info('frame2', frame2)
    print(frame2)
    # Массив frame2: <class 'pandas.core.frame.DataFrame'> 42285712 (6, 4)
    # year   state  pop  debt
    # one    2000    Ohio  1.5   0.0
    # two    2001    Ohio  1.7   1.0
    # three  2002    Ohio  3.6   2.0
    # four   2001  Nevada  2.4   3.0
    # five   2002  Nevada  2.9   4.0
    # six    2003  Nevada  3.2   5.0

    separator()

    # При присваивании столбцу списка или массива, их длина должна быть той же,
    # что и длинаDataFrame.
    # Если присваивать объект Series, то его метки будут выровнены по индексу
    # DataFrame, при этом будут вставляться отсутствующие значения для любых
    # «дыр»:
    val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
    frame2['debt'] = val
    arr_info('frame2', frame2)
    print(frame2)
    # Массив frame2: <class 'pandas.core.frame.DataFrame'> 42351296 (6, 4)
    # year   state  pop  debt
    # one    2000    Ohio  1.5   NaN
    # two    2001    Ohio  1.7  -1.2
    # three  2002    Ohio  3.6   NaN
    # four   2001  Nevada  2.4  -1.5
    # five   2002  Nevada  2.9  -1.7
    # six    2003  Nevada  3.2   NaN

    separator()

    # При присваивании отсутствующего столбца в объекте DataFrame добавится
    # новый столбец.
    # Ключевое слово del удаляет столбец, как и для словарей:
    frame2['eastern'] = frame2.state == 'Ohio'
    arr_info('frame2', frame2)
    print(frame2)
    # Массив frame2: <class 'pandas.core.frame.DataFrame'> 42351296 (6, 5)
    # year   state  pop  debt  eastern
    # one    2000    Ohio  1.5   NaN     True
    # two    2001    Ohio  1.7  -1.2     True
    # three  2002    Ohio  3.6   NaN     True
    # four   2001  Nevada  2.4  -1.5    False
    # five   2002  Nevada  2.9  -1.7    False
    # six    2003  Nevada  3.2   NaN    False

    # Предупреждение !!!
    # Новый столбец не может быть добавлен с помощью синтаксиса
    # frame2.eastern.
    print("frame2.columns:")
    print(frame2.columns)
    # Index(['year', 'state', 'pop', 'debt', 'eastern'], dtype='object')

    separator()

    del frame2['eastern']
    arr_info('frame2', frame2)
    print(frame2)
    # Массив frame2: <class 'pandas.core.frame.DataFrame'> 42613440 (6, 4)
    # year   state  pop  debt
    # one    2000    Ohio  1.5   NaN
    # two    2001    Ohio  1.7  -1.2
    # three  2002    Ohio  3.6   NaN
    # four   2001  Nevada  2.4  -1.5
    # five   2002  Nevada  2.9  -1.7
    # six    2003  Nevada  3.2   NaN
    print("frame2.columns:")
    print(frame2.columns)
    # Index(['year', 'state', 'pop', 'debt'], dtype='object')

    # Предупреждение !!!
    #
    # Столбец, возвращаемый при индексации DataFrame, является представлением
    # данных, а не копией. Таким образом, любые изменения в объекте Series
    # будут отражены в объекте DataFrame. Столбец можно явно скопировать
    # с помощью метода Series.copy.

    separator()

    # Другой распространенной формой представления данных является вложенный
    # словарь словарей.
    # Если вложенный словарь передать в конструктор DataFrame, pandas
    # интерпретируетключи внешнего словаря как столбцы, а внутренние ключи —
    # как индексы:
    pop = {'Nevada': {2001: 2.4, 2002: 2.9},
           'Ohio': {2001: 1.7, 2002: 3.6, 2000: 1.5},
           }
    frame3 = pd.DataFrame(pop)
    arr_info('frame3', frame3)
    print(frame3)
    # Массив frame3: <class 'pandas.core.frame.DataFrame'> 188669136 (3, 2)
    # Nevada  Ohio
    # 2001     2.4   1.7
    # 2002     2.9   3.6
    # 2000     NaN   1.5

    separator()

    # Можно транспонировать DataFrame:
    print(frame3.T)
    #         2001  2002  2000
    # Nevada   2.4   2.9   NaN
    # Ohio     1.7   3.6   1.5

    separator()

    # Можно задать порядок индексов:
    print(pd.DataFrame(pop, index=[2001, 2002, 2003]))
    #       Nevada  Ohio
    # 2001     2.4   1.7
    # 2002     2.9   3.6
    # 2003     NaN   NaN

    separator()

    # Словари рядов обрабатываются практически также:
    pdata = {'Ohio': frame3['Ohio'][:-1],
             'Nevada': frame3['Nevada'][:3]
             }
    print(pd.DataFrame(pdata))
    #       Ohio  Nevada
    # 2000   NaN     NaN
    # 2001   1.7     2.4
    # 2002   3.6     2.9

    # Полный список параметров, которые можно передавать в конструктор
    # DataFrame, можно найти в таблице 1. (в конце файла)

    separator()

    # Если для индекса и столбцов DataFrame установлены атрибуты name,
    # они также будут отображены:
    frame3.index.name = 'year'
    frame3.columns.name = 'state'
    print(frame3)
    # state  Nevada  Ohio
    # year
    # 2001      2.4   1.7
    # 2002      2.9   3.6
    # 2000      NaN   1.5

    separator()

    # Как и в случае Series, атрибут values возвращает данные, содержащиеся
    # в DataFrame, в виде двумерного массива:
    print(frame3.values)
    # [[2.4 1.7]
    #  [2.9 3.6]
    #  [nan 1.5]]


if __name__ == '__main__':
    main()

# Таблица 1: Возможные входные данные для конструктора DataFrame

# ----------------------------------------------------------------------------
# Тип               | Примечания
# ----------------------------------------------------------------------------
# Двумерный         | Матрица данных, передающаяся с необязательными метками
# ndarray           | строк и столбцов
# ----------------------------------------------------------------------------
# dict массивов,    | Каждая последовательность становится столбцом в
# list, tuple       | DataFrame. Все последовательности должны быть одинаковой
#                   | длины
# ----------------------------------------------------------------------------
# Структурированный | Обрабатывается как предыдущий случай
# массив (или мас-  |
# сив записей)      |
# ----------------------------------------------------------------------------
# dict объектов     | Каждое значение становится столбцом. Индексы из каждой
# типа Series       | серии объединяются вместе, чтобы сформировать индекс
#                   | строки результата, если не передан явный индекс
# ----------------------------------------------------------------------------
# dict объектов     | Каждый внутренний словарь становится стобцом. Ключи
# типа dict         | объединяются для формирования индекса строки, как
#                   | в предыдущем случае
# ----------------------------------------------------------------------------
# list объектов     | Каждый элемент становится строкой в DataFrame. Объедине-
# dict или Series   | ние ключей dict или индексов Series становится метками
#                   | столбцов DataFrame
# ----------------------------------------------------------------------------
# list объектов     | Обрабатывается как случай двумерного массива
# list или tuple    |
# ----------------------------------------------------------------------------
# DataFrame         | Используются индексы DataFrame, если не переданы другие
# ----------------------------------------------------------------------------
# маскированный     | Как случай двумерного массива, за исключением того, что
# массив NumPy      | маскированные значения становятся пропущенными (NA)
#                   | значениями в итоговом DataFrame
# ----------------------------------------------------------------------------
