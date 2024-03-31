import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
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



