import splunklib.client as client
import json
# Set variables 
HOST = ""
PORT = 8089 # Default Splunk port
USERNAME = "" # Splunk username
PASSWORD = "" # Splunk password
KV_STORE = "" # Name of KV store
APP = "" # App that the KV store resides in
# Create Splunk service
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD,
    owner="nobody",
    app=APP)
# Connect to Splunk KV Store
kvstore = service.kvstore[KV_STORE]
# Create data payload
output = {}
# Keys are normally auto generated but can be manually set
output['_key'] = '{}_{}'.format(data.get('key_part1'), data.get('key_part2'))
output['key1'] = data.get('key1')
output['key2'] = data.get('key2')
# To update or insert a record you must first check if the record exists
try:
    # Query KV store by ID
    # This will return an error if it does not exist or the row's data if it does
    test = kvstore.data.query_by_id(output['_key'])
    # Update record with new data
    kvstore.data.update(output['_key'], json.dumps(output))
except splunklib.binding.HTTPError as e:
    # If the test query fails then the record does not exist and needs to be insterted
    kvstore.data.insert(json.dumps(output))
