import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), "
          "GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: "
          "1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # indicate specific start and end dates for analysis
    print("Если в заданном периоде нужно указать конкретные даты начала и окончания для анализа, то укажите их")
    print("Или нажмите 'ENTER' для продолжения без конкретных дат для анализа")
    specific_dates = input("Введите дату начала и окончания периода "
                           "(например 2023-10-18:2023-10-23 или 2023-10-18 ), "
                           "или нажмите 'ENTER': "
                           )
    if not specific_dates:
        specific_dates = None
    else:
        specific_dates = specific_dates.split(':')

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period, specific_dates)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Calculates and displays the average closing price of shares for a given period
    dd.calculate_and_display_average_price(stock_data)

    # Analyzes data and notifies the user if the stock price has fluctuated by more than a specified percentage over a period
    print("Для получения уведомления изменения цены акции в заданном проценте")
    threshold = input("Введите порог максимальное и минимальное значения цены (например 10) ")
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Export data to CSV
    print("Для сохранения данных в CSV файл укажите имя")
    filename = input()
    dd.export_data_to_csv(stock_data, filename)
    print(f"Файл сохранен с именем <{filename}>")

    # Plot the RSI and MACD
    rsi = dd.rsi(stock_data)
    macd = dd.macd(stock_data)
    dplt.create_plot_macd_rsi(stock_data, rsi, macd, ticker, period)

    # Daily return in closing price and standard deviation of closing price
    print("Так же есть возможность произвести расчет и построить график дневной доходности и "
          "стандартное отклонение цены закрытия")
    print("При это необходимости укажите что нужно построить. Например:")
    print("1 - График дневной доходности цены закрытия")
    print("2 - Стандартное отклонение цены закрытия")
    print("3 - Если построить и тот и другой график")
    print("Или нажмите 'ENTER' для продолжения")
    choice = input(">>>")
    if choice == '':
        pass
    elif choice == '1':
        stock_data = dd.close_pct(stock_data)
        dplt.create_close_pct(stock_data, ticker, period)
    elif choice == '2':
        stock_data = dd.close_pct(stock_data)
        dplt.create_standard_deviation(stock_data, ticker, period)
    elif choice == '3':
        stock_data = dd.close_pct(stock_data)
        dplt.create_close_pct(stock_data, ticker, period)
        dplt.create_standard_deviation(stock_data, ticker, period)
    else:
        print('Указано не верное значение! Нужно 1, 2 или 3!')

    # Create interactive "plotly" graphs
    print("Уважаемый мой друг, я также могу построить для тебя интерактивныЙ график с помощью библиотеки 'Plotly' :)")
    print("Для этого тебе нужно выбрать нажать 'ПРОБЕЛ' или 'ENTER' для завершения")
    if input() != '':
        dd.close_pct(stock_data)
        dplt.create_plotly(stock_data)
    else:
        quit()
    quit()


if __name__ == "__main__":
    main()
