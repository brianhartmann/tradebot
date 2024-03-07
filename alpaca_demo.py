from alpaca.data.live import StockDataStream
import os
from dotenv import load_dotenv

load_dotenv() #loads env file
stream = StockDataStream(os.getenv("alpaca_key"), os.getenv("alpaca_secret")) #connects to alpaca

async def handle_trade(data):
    print(data.price)

stream.subscribe_trades(handle_trade, "AAPL") #subscribes to receive AAPL trade updates

stream.run()





