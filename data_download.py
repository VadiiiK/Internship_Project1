import yfinance as yf


def fetch_stock_data(ticker, period, specific_dates=None):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    if specific_dates is None:
        return data
    else:
        if len(specific_dates) == 2:
            try:
                df = data[specific_dates[0]:specific_dates[1]]
                return df
            except:
                print("Указан не коректно даты периода")
                return data
        elif len(specific_dates) == 1:
            print("Так как задана одна, период анализа будет от этой даты")
            try:
                df = data[specific_dates[0]:]
                return df
            except:
                print(f"Указана не коректно дата {specific_dates}, не как в примере!")
                return data
        else:
            print("Введеные данные заданны не как в примере")
            return data


def add_moving_average(data, window_size=5):
    data = data.fillna(0)
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    data = data['Close'].mean()
    return print(f'Средняя цена закрытия акций за указанный период равна: {data}')


def notify_if_strong_fluctuations(data, threshold):
    res = None
    data_max_value = data['Close'].max()
    data_min_value = data['Close'].min()
    percent_min_value = data_min_value * (float(threshold) / 100)
    if data_max_value - data_min_value > percent_min_value:
        res = 'Цена акций колебалась более чем на заданный процент за указанный период'
    return print(res)


def export_data_to_csv(data, filename):
    data.to_csv(f'{filename}.csv')


def rsi(df, periods=14, ema=True):
    """
    Возвращает pd.Series с индексом относительной силы.
    """
    close_delta = df['Close'].diff()
    # Делаем две серий: одну для низких закрытий и одну для высоких закрытий
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)

    if ema == True:
        # Использование экспоненциальной скользящей средней
        ma_up = up.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
        ma_down = down.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
    else:
        # Использование простой скользящей средней
        ma_up = up.rolling(window=periods, adjust=False).mean()
        ma_down = down.rolling(window=periods, adjust=False).mean()

    rsi = ma_up / ma_down
    rsi = 100 - (100 / (1 + rsi))
    return rsi


def macd(data):
    df = data
    df = df[['Close']]
    df.reset_index(level=0, inplace=True)
    df.columns = ['ds', 'y']
    exp1 = df.y.ewm(span=12, adjust=False).mean()
    exp2 = df.y.ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    return macd