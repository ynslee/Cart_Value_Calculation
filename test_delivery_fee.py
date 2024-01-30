from lib.delivery_fee import DeliveryCart, CartValueException, CalculateDistanceException, TimestampException, IntegerValueException
import pytest

def test_default_case():
	new_cart = DeliveryCart(790, 2235, 4, "2024-01-15T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 710

def test_small_cart_value_case():
	new_cart = DeliveryCart(640, 2235, 4, "2024-01-15T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 860

def test_short_distance_case():
	new_cart = DeliveryCart(1200, 450, 4, "2024-01-17T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 200

def test_long_distance_case1():
	new_cart = DeliveryCart(1200, 1499, 4, "2024-01-17T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 300

def test_long_distance_case2():
	new_cart = DeliveryCart(1200, 1500, 4, "2024-01-17T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 300

def test_long_distance_case3():
	new_cart = DeliveryCart(1200, 1501, 4, "2024-01-17T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 400

def test_long_distance_case4():
	new_cart = DeliveryCart(1200, 10000, 4, "2024-01-17T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 1500

def test_extra_item_case1():
	new_cart = DeliveryCart(1200, 1000, 5, "2024-01-17T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 250

def test_extra_item_case2():
	new_cart = DeliveryCart(1200, 1000, 10, "2024-01-17T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 500

def test_extra_item_case3():
	new_cart = DeliveryCart(1200, 1000, 13, "2024-01-17T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 770

def test_extra_item_case4():
	new_cart = DeliveryCart(1200, 1000, 14, "2024-01-17T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 820

def test_extra_item_case5():
	new_cart = DeliveryCart(1200, 1000, 27, "2024-01-17T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 1470

def test_extra_item_case6():
	new_cart = DeliveryCart(1200, 1000, 28, "2024-01-17T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 1500

def test_delivery_free():
	new_cart = DeliveryCart(20000, 1000, 28, "2024-01-17T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 0

def test_delivery_not_free():
	new_cart = DeliveryCart(19999, 1000, 27, "2024-01-17T13:00:00Z")
	assert new_cart.calculate_delivery_fee() == 1470

def test_delivery_everything_zero():
	with pytest.raises(CartValueException):
		new_cart = DeliveryCart(0, 0, 0, "2024-01-17T13:00:00Z")
		new_cart.calculate_delivery_fee() == 1470

def test_cart_value_exception():
	with pytest.raises(CartValueException):
		new_cart = DeliveryCart(-1, 2235, 4, "2024-01-15T13:00:00Z")
		new_cart.calculate_delivery_fee()

def test_calculate_distance_exception():
	with pytest.raises(CalculateDistanceException):
		new_cart = DeliveryCart(100, -1, 4, "2024-01-15T13:00:00Z")
		new_cart.calculate_delivery_fee()

def test_timestamp_exception1():
	with pytest.raises(TimestampException):
		new_cart = DeliveryCart(100, 100, 4, "999-01-15T13:00:00Z")
		new_cart.calculate_delivery_fee()

def test_timestamp_exception2():
	with pytest.raises(TimestampException):
		new_cart = DeliveryCart(100, 100, 4, "2024-01-15T13:-1:00Z")
		new_cart.calculate_delivery_fee()

def test_integer_value_case1():
	with pytest.raises(IntegerValueException):
		new_cart = DeliveryCart(640.0, 2235, 4, "2024-01-15T13:00:00Z")
		new_cart.calculate_delivery_fee()

def test_integer_value_case2():
	with pytest.raises(IntegerValueException):
		new_cart = DeliveryCart(640, 2235.0, 4, "2024-01-15T13:00:00Z")
		new_cart.calculate_delivery_fee()

def test_integer_value_case3():
	with pytest.raises(IntegerValueException):
		new_cart = DeliveryCart(640, 2235, 4.0, "2024-01-15T13:00:00Z")
		new_cart.calculate_delivery_fee()

