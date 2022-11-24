import requests
from get_price import get_best_price

def payload_exchange_routing(args):
    if 'amount' in args:
        try:
            amount = float(args['amount'])
            if amount <= 0:
            	return "ERROR: Enter a valid amount"
        except:
            return "ERROR: Amount is not a number. Please enter a number"
    else:
        return "ERROR: No amount field provided. Please specify an amount"

    try:
    	return get_best_price(amount)
    except:
    	return {"btcAmount": None,"usdAmount": None ,"Exchange":None}