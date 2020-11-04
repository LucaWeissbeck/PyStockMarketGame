import yfinance as yf

from swagger_server.models import StockValue, StockDescription
from swagger_server.services.db_service import DatabaseConn

"""

"""
# print(staticglobaldb.dbconn.get_transactions_and_stock_by_user(User(id=3)))

# stocks = (
# "ADS.DE", "ALV.DE", "BAS.DE", "BAYN.DE", "BEI.DE", "BMW.DE", "CON.DE", "1COV.DE", "DAI.DE", "DHER.DE", "DKB.DE",
# "DB1.DE", "DPW.DE", "DTE.DE", "DWNI.DE", "EOAN.DE", "FRE.DE", "FME.DE", "HEI.DE", "HEN3.DE", "IFX.DE", "LIN.DE",
# "MRK.DE", "MTX.DE", "MUV2.DE", "RWE.DE", "SAP.DE", "SIE.DE", "VOW3.DE", "VNA.DE")


def insert_stock_history_from_yfinance_to_db(symbol: str, period: str):
    """This function takes the symbol and period of a stock and sends the
        data as a StockValue model to the function DatabaseConn.insert_course()


    :param symbol: the ticker of the Stock
    :param period: The period of which the data is requested from the API
                (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
                re.sub(regex, string, replace)

    """
    df = yf.Ticker(symbol).history(period)
    conn = DatabaseConn()

    value = None
    for index, row in df.iterrows():
        open_value = row['Open']
        if open_value is None:
            continue
        date = index
        value = StockValue(None, symbol, float(open_value), str(date))
        conn.insert_course(value)
    return value


def get_stock_history_to_frontend(symbol: str, period: str):
    """This function takes the symbol and period of a stock and sends the
        data as a StockValue model to the function DatabaseConn.insert_course()


    :param symbol: the ticker of the Stock
    :param period: The period of which the data is requested from the API
                (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
                re.sub(regex, string, replace)

    """
    if symbol == "IBM":
        df = yf.Ticker(symbol).history(period)
        returned = []
        multiplier = 1
        for index, row in df.iterrows():
            open_value = row['Open']*multiplier
            if open_value is None:
                continue
            date = index
            returned.append(StockValue(None, symbol, float(open_value), str(date)))
            multiplier+=0.1
        return returned

    if symbol == "DDAIF":
        df = yf.Ticker(symbol).history(period)
        returned = []
        multiplier = 1.4
        for index, row in df.iterrows():
            open_value = row['Open']*multiplier
            if open_value is None:
                continue
            date = index
            returned.append(StockValue(None, symbol, float(open_value), str(date)))
            multiplier-=0.1
        return returned

    df = yf.Ticker(symbol).history(period)
    returned = []
    for index, row in df.iterrows():
        open_value = row['Open']
        if open_value is None:
            continue
        # close = row['Close']
        # high = row['High']
        # low = row['Low']
        date = index
        returned.append(StockValue(None, symbol, float(open_value), str(date)))
    return returned


def get_stock_data_from_db(symbol: str, period: str):
    print(symbol)
    print(period)
    pass


def get_stock_info_from_yfinance(symbol: str):
    """

    :param symbol:
    :return:
    """
    info = yf.Ticker(symbol).info
    for i in info:
        if info[i] is None:
            info[i] = "N/A"

    description = StockDescription(symbol, info['shortName'], info['country'], info['logo_url'], info['longBusinessSummary'], info['industry'], info['trailingAnnualDividendYield'], info['marketCap'], info['fiftyTwoWeekLow'], info['fiftyTwoWeekHigh'], info['fullTimeEmployees'])

    print(description)
    conn = DatabaseConn()
    success = conn.update_stock(description)
    print("Status: ", success)
    return description


#insert_stock_history_from_yfinance_to_db("IBM", "1d")
