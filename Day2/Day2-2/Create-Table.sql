create EXTERNAL TABLE IF NOT EXISTS <DB_name>.<TABLE_name> (
  `timestamp` string,
  `host` string,
  `port` int,
  `method` string,
  `path` string,
  `status_code` int
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://s3-bucket-name/'
TBLPROPERTIES ('skip.header.line.count'='1');