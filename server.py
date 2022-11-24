import flask
from flask import request
from request_handler import payload_exchange_routing

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "GET request on /exchange-routing\?amount={amount}"

@app.route('/exchange-routing', methods=['GET'])
def exchange_routing():
    return payload_exchange_routing(request.args)

app.run()