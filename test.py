import json
from pymongo import MongoClient

client = MongoClient("mongodb://user:password@example.com/?authSource=the_database&authMechanism=SCRAM-SHA-1")
db = client['HealthApp']
users = db['Users']

new_data = {
	'userId': 0,
	'access': 'admin',
	'name': 'Bruce Xiang',
	'role': 'admin',
	'temperature': 'none',
	'bloodPressure': 'none',
	'pulse': 'none',
	'oximeter': 'none',
	'weight': 'none',
	'glucometer': 'none'
}

users.insert_one(new_data)