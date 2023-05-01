from Data import Data
from Indicators import Indicators
import matplotlib.pyplot as plt
import mplfinance as mpf
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import random as random


def draw(indicator, data, symb, ind):
    plt.style.use('fivethirtyeight')
    plt.rcParams['figure.figsize'] = (20, 10)
    ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
    ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)
    ax1.plot(data['Close'], linewidth=2)
    ax1.set_title(symb)
    ax2.plot(indicator, color=(random.random(), random.random(), random.random()), linewidth=1)
    ax2.set_title(ind)
    plt.show()

class Project_run:
    @staticmethod
    def project_run():
        my_indicators = ['CCI', 'EVM', 'SMA', 'EWMA', 'ROC', 'BBANDS', 'ForceIndex', 'RSI']
        symb = input('Ведите монету для анализа:\n')
        begin = input('Дата начала анализа в формате YYYY-MM-DD:\n')
        end = input('Дата конца анализа в формате YYYY-MM-DD:\n')
        indicators = input('Введите список необходимых индикаторов:\n').split()
        a = Data()
        b = Indicators()
        data = a.candlesusdt(symb, begin, end)
        print(data)
        for elem in indicators:
            if elem not in my_indicators:
                print('no such indicator', elem)
                raise Exception
            if(elem == 'CCI'):
                draw(b.CCI(data), data, symb, 'CCI')
            elif(elem == 'EVM'):
                draw(b.EVM(data), data, symb, 'EVM')
            elif (elem == 'SMA'):
                draw(b.SMA(data), data, symb, 'SMA')
            elif(elem == 'EWMA'):
                draw(b.EWMA(data), data, symb, 'EWMA')
            elif(elem == 'ROC'):
                draw(b.ROC(data), data, symb, 'ROC')
            elif (elem == 'BBANDS'):
                draw(b.BBANDS(data), data, symb, 'BBANDS')
            elif (elem == 'ForceIndex'):
                draw(b.ForceIndex(data), data, symb, 'ForceIndex')
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
