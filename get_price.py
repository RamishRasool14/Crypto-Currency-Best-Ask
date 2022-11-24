import requests
import numpy as np

def filter_ask_price(ask, amount ,order_by = 1):
    filtered = ask[ask[:,1] >= amount ]
    filtered = filtered[filtered[:, order_by].argsort()]
    return filtered

def get_best_price(amount):
    exchanges = ["Binance", "Coinbase", "FTX"]
    BTC_API = "https://api.binance.com/api/v3/depth?symbol=BTCUSDT&limit=5000"
    COINBASE_API = "https://api.exchange.coinbase.com/products/BTC-USDT/book?level=2"
    FTX_API =  "https://ftx.com/api/markets/BTC/USDT/orderbook?depth=100"

    response = requests.get(BTC_API)
    binance_ask = np.array(response.json()["asks"],dtype = float)
    
    response = requests.get(url = COINBASE_API, headers={"accept": "application/json"})
    coinbase_ask = np.array(response.json()["asks"],dtype = float)
    
    response = requests.get(FTX_API)
    ftx_ask = np.array(response.json()["result"]["asks"],dtype = float)
    
    filtered_binance = filter_ask_price(binance_ask, amount)
    filtered_coinbase = filter_ask_price(coinbase_ask, amount)
    filtered_ftx = filter_ask_price(ftx_ask, amount)
    
    filtered_exchange_order_books = [filtered_binance, filtered_coinbase, filtered_ftx]
    
    lowest_asks = []
    count = 0
    for filtered in filtered_exchange_order_books:
        if len(filtered) != 0:
            lowest_asks.append(filtered[0,0])
        else:
            count = count + 1
            lowest_asks.append(float('inf'))
            
    min_index = lowest_asks.index(min(lowest_asks))
    btcAmount = filtered_exchange_order_books[min_index][0,1]
    usdAmount = filtered_exchange_order_books[min_index][0,0]
    Exchange = exchanges[min_index]
    
    return {"btcAmount": btcAmount,"usdAmount": usdAmount ,"Exchange":Exchange}

