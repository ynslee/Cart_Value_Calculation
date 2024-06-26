from datetime import datetime
import math

class CartValueException(Exception):
	pass

class CalculateDistanceException(Exception):
	pass

class TimestampException(Exception):
	pass

class IntegerValueException(Exception):
	pass

class DeliveryCart:

	def __init__(self, cart_value, delivery_distance, number_of_items, time : str) -> None:
		if isinstance(cart_value, int):
			self._cart_value : int = cart_value
		else:
			raise IntegerValueException("Value is not an Integer")
		if isinstance(delivery_distance, int):
			self._delivery_distance : int = delivery_distance
		else:
			raise IntegerValueException("Value is not an Integer")
		if isinstance(number_of_items, int):
			self._number_of_items : int = number_of_items
		else:
			raise IntegerValueException("Value is not an Integer")
		self._time = time

	def _check_cart_value(self):
		if (self._cart_value < 1000) and (self._cart_value > 0):
			return 1000 - self._cart_value
		elif (self._cart_value <= 0):
			raise CartValueException("Cart value could not be a negative or zero value")
		else:
			return 0
	
	def _calculate_delivery_distance(self):
		if (self._delivery_distance <= 0):
			raise CalculateDistanceException("distance could not be a negative or zero value")
		if (self._delivery_distance <= 1000):
			return 200
		elif (self._delivery_distance > 1000):
			_distance_fee : int = 200
			distance = self._delivery_distance - 1000
			if distance % 500 == 0:
				fee_multiplier = math.floor(distance / 500)
			else:
				fee_multiplier = math.floor(distance / 500) + 1
			_distance_fee += fee_multiplier * 100	
			return _distance_fee

	def _calculate_bulk_fees(self):
		if (self._number_of_items < 5):
			return 0
		number_items = self._number_of_items - 5
		_surcharge : int = 0
		while number_items >= 0:
			_surcharge += 50
			number_items -= 1
		if (self._number_of_items > 12):
			_surcharge += 120
		return _surcharge

	def calculate_delivery_fee(self):
		surcharge = self._check_cart_value()
		delivery_fee = self._calculate_delivery_distance()
		surcharge += self._calculate_bulk_fees()
		delivery_fee += surcharge
		try:
			order_time = datetime.strptime(self._time, "%Y-%m-%dT%H:%M:%SZ")
		except Exception:
			raise TimestampException("Date time is not valid")
		if (order_time.weekday() == 4):
			if(order_time.hour >= 15) and (order_time.hour < 19):
				delivery_fee = delivery_fee * 1.2
		if (delivery_fee > 1500):
			delivery_fee = 1500
		if (self._cart_value >= 20000):
			delivery_fee = 0
		return int(delivery_fee)
