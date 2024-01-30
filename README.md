# Wolt Delivery Fee Calculator 🛒

This is Delivery fee calculator for the backend assignment belongs to Yoonseon Lee

## Table of Contents
- 1\. [Getting Started](#getting_started)
	- [Setup virtual environment](#1-setup-virtual-environment)
	- [Activite virtual environment](#2-activite-virtual-environment)
	- [Install needed configuraration files](#3-install-needed-configuraration-files)
- 2\. [Run Flask to see working API](#run_flask)
- 3\. [Run Test](#run_test)

## Getting started 🏁 <a name = "getting_started"></a>
Follow the instruction to use delivery calculator 

### Prerequisities

#### 1\. Setup virtual environment
Python should be upgrade to Python 3.6 or upper before running the following command
```
$ python -m venv myvenv
```
#### 2\. Activite virtual environment
```
$ source myvenv/bin/activate
```
#### 3\. Install needed configuraration files
For the assignment requirements
```
$ pip -r requirements.txt
```
If you wish to use test_delivery_fee.py file to test, please install requirement_test.txt as well
```
$ pip -r requirement_test.txt
```
### Run Flask to see working API <a name = "run_flask"></a>

Run the command in the same directory as all the files are

```
$ flask --app . run
```
Request should be as folllowing order. Keys should be remained as the same, values can be modified 
```json
{"cart_value": 10, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}
```
##### Field details

| Field             | Type  | Description                                                               | Example value                             |
|:---               |:---   |:---                                                                       |:---                                       |
|cart_value         |Integer|Value of the shopping cart __in cents__.                                   |__790__ (790 cents = 7.90€)                |
|delivery_distance  |Integer|The distance between the store and customer’s location __in meters__.      |__2235__ (2235 meters = 2.235 km)          |
|number_of_items    |Integer|The __number of items__ in the customer's shopping cart.                   |__4__ (customer has 4 items in the cart)   |
|time               |String |Order time in UTC in [ISO format](https://en.wikipedia.org/wiki/ISO_8601). |__2024-01-15T13:00:00Z__                   |

Tip🔧 Use Thunder Client tool on VScode to check if it returns the proper value when values are given

### Run test <a name = "run_test"></a>

If you have installed [the requirement configuration files](#3-install-needed-configuraration-files) for the test_deliver_fee.py, you can run the command
```
$ pytest
```