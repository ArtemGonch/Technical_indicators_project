from Indicators import Indicators
import numpy as np
import unittest
import yfinance as yf

data1 = yf.download('BTC', start='2022-01-01', end='2023-01-01')
#2022-01-01 Open: 98.309998 High: 98.309998 Low: 98.294701 Close: 98.294701
tmp1 = data1.iloc[0]
#2022-12-23 Open: 90.771004 High: 90.804497 Low: 90.760002 Close: 90.804497
tmp2 = data1.iloc[246]
class IndicatorsTest(unittest.TestCase):
    #checking BTC
    def testCCI(self):
        tmp = Indicators()
        self.assertTrue(np.isnan(tmp.CCI(tmp1)))
        self.assertEqual(tmp.CCI(tmp2), -101.076218)
    def testEVM(self):
        tmp = Indicators()
        self.assertTrue(np.isnan(tmp.EVM(tmp1)))
        self.assertEqual(tmp.EVM(tmp2), -2202.824389)
    def testSMA(self):
        tmp = Indicators()
        self.assertTrue(np.isnan(tmp.SMA(tmp1)))
        self.assertEqual(tmp.SMA(tmp2), 91.346410)
    def testEWMA(self):
        tmp = Indicators()
        self.assertEqual(np.isnan(tmp.EWMA(tmp1)))
        self.assertEqual(tmp.EWMA(tmp2), 91.192543)
    def testROC(self):
        tmp = Indicators()
        self.assertEqual(np.isnan(tmp.ROC(tmp1)))
        self.assertEqual(tmp.ROC(tmp2), -0.005579)
    def testForceIndex(self):
        tmp = Indicators()
        self.assertEqual(np.isnan(tmp.ForceIndex(tmp1)))
        self.assertEqual(tmp.ROC(tmp2), -666.304413)
    def testRSI(self):
        tmp = Indicators()
        self.assertEqual(np.isnan(tmp.RSI(tmp1)))
        self.assertEqual(tmp.RSI(tmp.ROC(tmp2)), 43.156718)