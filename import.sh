#!/bin/bash

DB_USER="root"
DB_PASS="root"
DB_NAME="ibm"
TABLE_NAME="new_table"
CSV_FILE="/home/peekknuf/IBM_financial_data_intraday.csv"

mysql --local_infile=1 -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" <<EOF
LOAD DATA LOCAL INFILE '$CSV_FILE'
INTO TABLE $TABLE_NAME
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
EOF

# mysql> set global local_infile=true;
# secure_file_priv issues