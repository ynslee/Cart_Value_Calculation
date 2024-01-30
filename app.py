from flask import Flask, request, jsonify
from lib.delivery_fee import DeliveryCart
from marshmallow import Schema, fields, ValidationError
from datetime import datetime
import traceback

def isLargerThanZero(value: str):
	
	return value > 0

def isValidTimestamp(utcTs: str):
	try:
		datetime.strptime(utcTs, "%Y-%m-%dT%H:%M:%SZ")
		return True
	except Exception as e:
		return False

class DeliveryCartPayload(Schema):
	cart_value = fields.Integer(strict=True, required=True, validate=isLargerThanZero)
	delivery_distance = fields.Integer(strict=True, required=True, validate=isLargerThanZero)
	number_of_items = fields.Integer(strict=True, required=True, validate=isLargerThanZero)
	time = fields.String(validate=isValidTimestamp)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def delivery_fee():
	data = request.get_json()
	try:
		DeliveryCartPayload().load(data)
	except ValidationError as e:
		return jsonify(e.messages), 400
	try:
		cart = DeliveryCart(data['cart_value'], data['delivery_distance'], data['number_of_items'], data['time'])
		return jsonify({'delivery fee' : cart.calculate_delivery_fee()}), 200
	except Exception as e:
		print(e)
		print(traceback.format_exc())
		return jsonify({"error" : "Server error"}), 500