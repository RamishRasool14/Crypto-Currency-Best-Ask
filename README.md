# Crypto-Best-Ask Api

This api gets you the best ask price across 3 exchanges (Binance, Coinbase & FTX) for the amount of cryto that you want to sell. After successful setting up locally you can query api using endpoint ```http://localhost:{port}/exchange-routing?amount={amount}``` where your server is running on port and amount is the crypto amount BTC that you want to sell.

## Setting Up
1. Run ```pip install virtualenv``` in terminal if you do not have virtual env already installed. Assuming you already have pip and python setted up.
2. Create a virtual environment ```python3 -m venv /path/to/new/virtual/environment```
3. Source into the virtual env named 'venv' that you just created ```source venv/bin/activate```
4. Cd into the directory /backend
5. Run ```pip install -r requirements.txt```
6. Run ```python server.py```

Server will now be listening on http://localhost:{port}

7. Open another terminal and you can fetch data from api using ```http://localhost:{port}/exchange-routing?amount={amount}```

Where {amount} is the total amount of BTC you want to buy and {port} is the port number on which your server is listening on.

This will fetch asks from order books of 3 exchanges (Binance, Coinbase & FTX) and return the best ask price for you to buy with the amount and price on a particular exchange!

8. To execute unit test ```python -m unittest unit_test.py```

## Methodology

1. Fetched order book from coinbase and binance api
2. Filtered both order books for ask price
3. Filtered order books for the lowest ask amount that is just greater than the purchase amount
4. Compared prices for this amount from both order books and returned by the function
5. Setted up an API using Flask to fetch results from localhost url

## Assumptions
1. Price for the lowest ask amount in an order book that is just greater than the purchase amount is the price we are interested in.
