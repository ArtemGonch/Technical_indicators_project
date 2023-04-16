import yfinance as yf

class Data:
    @staticmethod
    def candlesusdt(symb, begin, end):
        data = yf.download(symb, start=begin, end=end)
        return data