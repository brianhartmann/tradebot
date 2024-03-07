# from alpaca.trading.client import TradingClient
# from alpaca.trading.requests import MarketOrderRequest
# from alpaca.trading.enums import OrderSide, TimeInForce

# trading_client = TradingClient("PKQ3W1FASCOB7DA4K7V5", "BzX3mYthrDL6Vd4XAjQGO1Pz4uI2TMUxE7hMxsIH")

# market_order_data = MarketOrderRequest(
#     symbol="AAPL",
#     qty = 1,
#     side=OrderSide.BUY,
#     time_in_force=TimeInForce.DAY
# )

# market_order = trading_client.submit_order(market_order_data)
# print(market_order)

from alpaca.data.live import StockDataStream

stream = StockDataStream("PKQ3W1FASCOB7DA4K7V5", "BzX3mYthrDL6Vd4XAjQGO1Pz4uI2TMUxE7hMxsIH")

async def handle_trade(data):
    print(data.price)

stream.subscribe_trades(handle_trade, "AAPL")

stream.run()





