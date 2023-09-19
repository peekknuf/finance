import requests
import config
import json

url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey='+config.api
r = requests.get(url)
raw_data = r.json()
json_data = json.dumps(raw_data, indent=4, sort_keys=True)

ibm = open('./json/ibm_statement.json', 'w')
ibm.write(json_data)