from pyspark.sql import SparkSession
import time


spark = SparkSession \
    .builder \
    .appName('standalone') \
    .getOrCreate()

schema = 'id INT, country STRING, hit LONG'
df = spark.createDataFrame(data=[(1,'Korea',120),(2,'USA',80), (3, 'Japan', 40)], schema=schema)
df.count()

# sleep 5 minute
time.sleep(600)