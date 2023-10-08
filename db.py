import mysql.connector
from tabulate import tabulate

host = "localhost"
user = "root"
password = "root"
database = "ibm"


connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
cursor = connection.cursor()

cursor.execute("SELECT * FROM new_table")

result = cursor.fetchall()
headers = ["Date", "Open", "High", "Low", "Close", "Volume"]
table = tabulate(result, headers, tablefmt="grid")

print(table)