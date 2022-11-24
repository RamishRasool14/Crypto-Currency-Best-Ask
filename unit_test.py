import unittest
from get_price import get_best_price
from request_handler import payload_exchange_routing

class TestAPI(unittest.TestCase):
	def test_get_price(self):
		result = get_best_price(1)
		assert isinstance(float(result["btcAmount"]), float) 
		assert isinstance(float(result["usdAmount"]), float) 
		assert result["Exchange"] in ["Binance", "Coinbase", "FTX"]

	def test_payload_exchange_routing(self):
		response = payload_exchange_routing({'amount':0})
		assert response == "ERROR: Enter a valid amount"
		response = payload_exchange_routing({'amount':"abc"})
		assert response == "ERROR: Amount is not a number. Please enter a number"
		response = payload_exchange_routing({'amount_error': 1})
		assert response == "ERROR: No amount field provided. Please specify an amount"
		response = payload_exchange_routing({'amount':2})
		assert response["Exchange"] in ["Binance", "Coinbase", "FTX"]