import pandas as pd

class Indicators:

    # Commodity Channel Index
    @staticmethod
    def CCI(data, days = 10):
        TP = (data['High'] + data['Low'] + data['Close']) / 3
        CCI = pd.DataFrame((TP - TP.rolling(days).mean()) / (0.015 * TP.rolling(days).std()))
        return CCI

    # Ease of Movement
    @staticmethod
    def EVM(data, days = 10):
        dm = ((data['High'] + data['Low']) / 2) - ((data['High'].shift(1) + data['Low'].shift(1)) / 2)
        br = (data['Volume'] / 100000000) / ((data['High'] - data['Low']))
        EVM = dm / br
        EVM_MA = pd.DataFrame(EVM.rolling(days).mean())
        return EVM_MA

    # Simple Moving Average
    @staticmethod
    def SMA(data, days = 10):
        SMA = pd.DataFrame(data['Close'].rolling(days).mean())
        return SMA

    # Exponentially-weighted Moving Average
    @staticmethod
    def EWMA(data, days = 10):
        EMA = pd.DataFrame(data['Close'].ewm(span=days, min_periods=days - 1).mean())
        return EMA

    # Rate of Change (ROC)
    @staticmethod
    def ROC(data, n = 10):
        N = data['Close'].diff(n)
        D = data['Close'].shift(n)
        ROC = pd.DataFrame(N / D)
        return ROC

    # Compute the Bollinger Bands
    @staticmethod
    def BBANDS(data, n = 10):
        MA = data.Close.rolling(n).mean()
        SD = data.Close.rolling(n).std()
        data['UpperBB'] = MA + (2 * SD)
        data['LowerBB'] = MA - (2 * SD)
        return data

    # Force Index
    @staticmethod
    def ForceIndex(data, days = 10):
        FI = pd.DataFrame(data['Close'].diff(days) * data['Volume'])
        return FI

    # RSI
    @staticmethod
    def RSI(data, n=10):
        change = data['Close'].diff()
        change.dropna(inplace=True)
        change_up = change.copy()
        change_down = change.copy()
        change_up[change_up < 0] = 0
        change_down[change_down > 0] = 0
        avg_up = change_up.rolling(14).mean()
        avg_down = change_down.rolling(14).mean().abs()
        rsi = 100 * avg_up / (avg_up + avg_down)
        return rsi