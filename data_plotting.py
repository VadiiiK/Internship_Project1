import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    print("Для применения стиля к графику нажмите 'ПРОБЕЛ' или 'ENTER'")
    if input() != '':
        print("Выберите ключ стиля к графику")
        print('Например: 1')
        print('Ключи стилей:')
        keys_style = {}
        for i in range(len(plt.style.available)):
            keys_style[i] = plt.style.available[i]
            print(i, '-', plt.style.available[i])
        try:
            plt.style.use(keys_style[int(input())])
        except:
            print("Ключ указанный вами не как указан в примере!")
            print("График будет построен без применения стиля")

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def create_plot_macd_rsi(data, rsi, macd, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, rsi, label='RSI')
            plt.plot(dates, macd, label='MACD')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], rsi, label='RSI')
        plt.plot(data['Date'], macd, label='MACD')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_average_closing_price.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def create_close_pct(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close_pct'].values, label='Daily return')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close_pct'], label='Daily return')

    plt.title(f"{ticker} Дневная доходность в цене закрытия акции")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_daily_return_in_closing_price.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def create_standard_deviation(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            plt.plot(data['Close_pct'].rolling(5).std(), label='Standard deviation')
            plt.plot(data['Close_pct'].rolling(7).mean(), label='Moving average daily return')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close_pct'].rolling(5).std(), label='Standard deviation')
        plt.plot(data['Date'], data['Close_pct'].rolling(7).mean(), label='Moving average daily return')

    plt.title(f"{ticker} Стандартное отклонение в цене закрытия акции")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_standard_deviation_of_closing_price.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")