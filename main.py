# Goncharov Artem Technical indicators project
import unittest
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import yfinance as yf
import requests
import numpy as np
import json
import datetime
import pandas as pd
import mplfinance as mpf
from Indicators import Indicators
from Data import Data

my_indicators = ['CCI', 'EVM', 'SMA', 'EWMA', 'ROC', 'BBANDS', 'ForceIndex', 'RSI']
symb = input()
begin = input()
end = input()
indicators = input().split()
a = Data()
b = Indicators()
data = a.candlesusdt(symb, begin, end)
print(data)
mpf.plot(data, type='candle', mav=(3, 6, 9), volume=True)
for elem in indicators:
    if elem not in my_indicators:
        print('no such indicator', elem)
        raise Exception
    if(elem == 'CCI'):
        plt.style.use('fivethirtyeight')
        plt.rcParams['figure.figsize'] = (20, 10)
        ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
        ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)
        ax1.plot(data['Close'], linewidth=2)
        ax1.set_title(symb)
        ax2.plot(b.CCI(data), color='orange', linewidth=1)
        ax2.set_title('CCI')
        plt.show()
    elif(elem == 'EVM'):
        plt.style.use('fivethirtyeight')
        plt.rcParams['figure.figsize'] = (20, 10)
        ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
        ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)
        ax1.plot(data['Close'], linewidth=2)
        ax1.set_title(symb)
        ax2.plot(b.EVM(data), color='orange', linewidth=1)
        ax2.set_title('EVM')
        plt.show()
    elif (elem == 'SMA'):
        plt.style.use('fivethirtyeight')
        plt.rcParams['figure.figsize'] = (20, 10)
        ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
        ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)
        ax1.plot(data['Close'], linewidth=2)
        ax1.set_title(symb)
        ax2.plot(b.SMA(data), color='orange', linewidth=1)
        ax2.set_title('SMA')
        plt.show()
    elif(elem == 'EWMA'):
        plt.style.use('fivethirtyeight')
        plt.rcParams['figure.figsize'] = (20, 10)
        ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
        ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)
        ax1.plot(data['Close'], linewidth=2)
        ax1.set_title(symb)
        ax2.plot(b.EWMA(data), color='orange', linewidth=1)
        ax2.set_title('EWMA')
        plt.show()
    elif(elem == 'ROC'):
        plt.style.use('fivethirtyeight')
        plt.rcParams['figure.figsize'] = (20, 10)
        ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
        ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)
        ax1.plot(data['Close'], linewidth=2)
        ax1.set_title(symb)
        ax2.plot(b.ROC(data), color='green', linewidth=1)
        ax2.set_title('ROC')
        plt.show()
    elif (elem == 'BBANDS'):
        plt.style.use('fivethirtyeight')
        plt.rcParams['figure.figsize'] = (20, 10)
        ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
        ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)
        ax1.plot(data['Close'], linewidth=2)
        ax1.set_title(symb)
        ax2.plot(b.BBANDS(data), color='purple', linewidth=1)
        ax2.set_title('BBANDS')
        plt.show()
    elif (elem == 'ForceIndex'):
        plt.style.use('fivethirtyeight')
        plt.rcParams['figure.figsize'] = (20, 10)
        ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
        ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)
        ax1.plot(data['Close'], linewidth=2)
        ax1.set_title(symb)
        ax2.plot(b.ForceIndex(data), color='red', linewidth=1)
        ax2.set_title('ForceIndex')
        plt.show()
    elif(elem == 'RSI'):
        plt.style.use('fivethirtyeight')
        plt.rcParams['figure.figsize'] = (20, 10)
        ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
        ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)
        ax1.plot(data['Close'], linewidth=2)
        ax1.set_title(symb)
        ax2.plot(b.RSI(data), color='orange', linewidth=1)
        ax2.axhline(30, linestyle = '--', linewidth=1.5, color='green')
        ax2.axhline(70, linestyle = '--', linewidth=1.5, color='red')
        ax2.set_title('RSI')
        plt.show()