from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.client import TradingClient
import os
from dotenv import load_dotenv

index=0
load_dotenv() #loads env file
trading_client = TradingClient(os.getenv("alpaca_key"), os.getenv("alpaca_secret"))

# def trading_algo_sell():
#     positions = trading_client.get_all_positions()
#     for stock in positions:
#         if (float(stock.market_value) > float(stock.cost_basis) * 1.005):
#             market_order_data=MarketOrderRequest(
#                 symbol="AAPL",
#                 qty=1,
#                 side=OrderSide.SELL,
#                 time_in_force=TimeInForce.DAY
#             )
#         elif (float(stock.market_value) < float(stock.cost_basis) * 0.995):
#             market_order_data=MarketOrderRequest(
#                 symbol="AAPL",
#                 qty=1,
#                 side=OrderSide.SELL,
#                 time_in_force=TimeInForce.DAY
#             )
#             market_order = trading_client.submit_order(market_order_data);
#             print(f'Sold one share of {market_order.symbol}.')


# def trading_algo_buy(values):
#     global index
#     price1 = values[index]
#     price2 = values[index+1]
#     price3 = values[index+2]
#     if (price3 > price2 and price2>price1):
#         market_order_data=MarketOrderRequest(
#             symbol="AAPL",
#             qty=1,
#             side=OrderSide.BUY,
#             time_in_force=TimeInForce.DAY
#         )
#         market_order = trading_client.submit_order(market_order_data);
#         print(f'Bought one share of {market_order.symbol}.')
#     index+=1

def make_trade(stock, order):
    side = 0
    if (order == 'purchase'):
        side = OrderSide.BUY
        market_order_data=MarketOrderRequest(
            symbol=stock,
            qty=10,
            side=side,
            time_in_force=TimeInForce.DAY
        )
        market_order = trading_client.submit_order(market_order_data)
        print(f'Successfully bought {market_order_data.qty} shares of {market_order.symbol}.\n')
    elif (order == 'sale'):
        side = OrderSide.SELL
        positions = 0
        try:
            positions = trading_client.get_open_position(stock)
        except:
            print('A sell order was made but no stock exists in our portfolio.')
            return
        market_order_data=MarketOrderRequest(
            symbol=stock,
            qty=positions.qty,
            side=side,
            time_in_force=TimeInForce.DAY
        )
        market_order = trading_client.submit_order(market_order_data)
        print(f'Successfully sold {market_order_data.qty} shares of {market_order.symbol}.\n')