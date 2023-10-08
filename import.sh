LOAD DATA LOCAL INFILE '/home/peekknuf/finance/IBM_financial_data_hourly.csv' INTO TABLE new_table
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 

# mysql> set global local_infile=true;
# secure_file_priv issues