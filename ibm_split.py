import json

with open('ibm_statement.json', 'r') as f:
    financial_statement = json.load(f)

annual_reports = []
quarterly_reports = []

for report in financial_statement['annualReports']:
    annual_reports.append(report)

for report in financial_statement['quarterlyReports']:
    quarterly_reports.append(report)

annual_reports_data = {'annualReports': annual_reports}
quarterly_reports_data = {'quarterlyReports': quarterly_reports}

with open('./json/annual_reports.json', 'w') as f:
    json.dump(annual_reports_data, f, indent=4)

with open('./json/quarterly_reports.json', 'w') as f:
    json.dump(quarterly_reports_data, f, indent=4)