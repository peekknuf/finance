import requests
import config
import csv
from io import StringIO 


company = 'IBM'

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=1min&apikey='+config.api+'&datatype=csv'

params = {
    "company_name": company,
    "api_key": config.api
    }

response = requests.get(url, params=params)
if response.status_code == 200:
    csv_data = response.text
    csv_reader = csv.reader(StringIO(csv_data))
    file_name = f"{company}_financial_data_hourly.csv"
        
    with open(file_name, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
            
        for row in csv_reader:
            csv_writer.writerow(row)
        
        print(f"CSV data downloaded and processed for {company}")
else:
        print(f"Failed to download data for {company}. Status code: {response.status_code}")