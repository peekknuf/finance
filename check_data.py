import pandas as pd
import json

with open('./json/annual_reports.json', 'r') as f:
    ann_rep_df = json.load(f)['annualReports']

annual_df = pd.json_normalize(ann_rep_df)
annual_df.to_csv('annual_df.csv', index=False)