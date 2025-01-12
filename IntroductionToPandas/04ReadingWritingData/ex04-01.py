# Pandas - Чтение и запись данных
#
# В библиотеке pandas реализованы функции чтения табличных данных в объект
# DataFrame. В таблице 7 представлены некоторые из таких функций.
import pandas as pd
# import pandas_datareader.data as web
import pandas_datareader as web


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
    # Нативная разработка — это создание приложений на родном языке платформы
    # и использование API/фреймворков, специально разработанных для доступа
    # к функциям устройства. Для Android это будет Java или Kotlin с его JDK,
    # а для iOS — Obj-C или Swift на iOS SDK.
    # Разработчики обычно предпочитают нативные приложения для высокопроизво-
    # дительных приложений, которые обеспечивают наилучшее взаимодействие
    # с пользователем.

    # Библиотека pandas поддерживает нативную работу со многими реляционными
    # БД. Можно не только загружать данные из локальных файлов, но и из
    # Интернета — достаточно вместо адреса на локальном компьютере указать
    # прямю ссылку на файл.
    # Также существует дополнительный пакет, который называется
    # pandas_datareader. Если он не установлен, его можно установить через
    # conda или pip. Он загружает данные из некоторых источников.

    # Загрузим с помощью pandas_datareader некоторые данные для некоторых
    # биржевых тикеров:

    all_data = {ticker: web.get_data_yahoo(ticker)
                for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}
    price = pd.DataFrame({ticker: data['Adj Close']
                          for ticker, data in all_data.items()})
    volume = pd.DataFrame({ticker: data['Volume']
                           for ticker, data in all_data.items()})

    # Вычислим процентные изменения цен:
    returns = price.pct_change()
    print(returns.tail())

    # Метод corr объекта Series вычисляет корреляцию перекрывающихся,
    # выровненных по индексу значений в двух объектах Series. Соответственно
    # cov вычисляет ковариацию:
    print(returns['MSFT'].corr(returns['IBM']))

    print(returns['MSFT'].cov(returns['IBM']))

    # Поскольку MSFT является допустимым атрибутом Python, мы также можем
    # выбрать эти столбцы, используя более краткий синтаксис
    print(returns.MSFT.corr(returns.IBM))

    # Методы corr и cov объекта DataFrame возвращают полные матрицы корреляции
    # или ковариации:
    print(returns.corr())

    print(returns.cov())

    # Используя метод corrwith объекта DataFrame, можно вычислять попарные
    # корреляции между столбцами или строками DataFrame с другими объектами
    # Series или DataFrame.Передача в качестве аргумента ряда возвращает ряд
    # со значением корреляции, вычисленным для каждого столбца:
    print(returns.corrwith(returns.IBM))


if __name__ == '__main__':
    main()
#  Таблица 7: Функции чтения данных
# ----------------------------------------------------------------------------
#  Функция          |  Описание
# ----------------------------------------------------------------------------
#  read_csv         |  Загружает разделённые значения из файла или файло-
#                   |  подобного объекта; в качестве разделителя по умолчанию
#                   |  используется запятая
# ----------------------------------------------------------------------------
#  read_table       |  Загружает разделённые значения из файла или файло-
#                   |  подобного объекта; в качестве заделителя по умолчанию
#                   |  используется табуляция ('\t')
# ----------------------------------------------------------------------------
#  read_fwf         |  Читает данные в формате со столбцами фиксированной
#                   |  длины (без разделителей)
# ----------------------------------------------------------------------------
#  read_clipboard   |  Версия функции read_table, которая читает данные из
#                   |  буфера обмена
# ----------------------------------------------------------------------------
#  read_excel       |  Читает данные из файлов формата .xls или .xlsx
# ----------------------------------------------------------------------------
#  read_hdf         |  Читает файлы формата HDF5, записанные с помощью
#                   |  библиотеки pandas
# ----------------------------------------------------------------------------
#  read_html        |  Читает все таблицы из заданного документа HTML
# ----------------------------------------------------------------------------
#  read_json        |  Читает данные из JSON (JavaScriptObjectNotation)
# ----------------------------------------------------------------------------
#  read_msgpack     |  Читает данные pandas закодированные с помощью двоичного
#                   |  формата MessagePack
# ----------------------------------------------------------------------------
#  read_pickle      |  Читает любой объект, сохранённый в формате
#                   |  Python pickle
# ----------------------------------------------------------------------------
#  read_sas         |  Читает набор данных SAS, хранящийся в одном из поль-
#                   |  зовательских форматов хранения системы SAS
# ----------------------------------------------------------------------------
#  read_sql         |  Читает результат запроса SQL (используя SQLAlchemy)
#                   |  как объекта DataFrame
# ----------------------------------------------------------------------------
