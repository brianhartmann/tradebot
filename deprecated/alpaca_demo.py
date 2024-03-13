from alpaca.data.live import StockDataStream
import os
from dotenv import load_dotenv
from algorithms import *

load_dotenv() #loads env file

#connect to alpaca for stock price and buy orders
stream = StockDataStream(os.getenv("alpaca_key"), os.getenv("alpaca_secret"))

#receives stock price and sends to trading algo
values = []

async def handle_trade(data):
    # trading_algo_sell()
    values.append(data.price)
    # if len(values) >= 3:
    #     trading_algo_buy(values)

print('Starting trading bot...')
stream.subscribe_trades(handle_trade, "AAPL") #subscribes to receive AAPL trade updates
stream.run()