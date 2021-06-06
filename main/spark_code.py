from  pyspark.sql.types import *
from pyspark.sql import SparkSession,Window
import pyspark.sql.functions as f
from pyspark.sql.types import *
import os
os.environ["JAVA_HOME"] = "/usr/local/java/jdk1.8.0_241/"


spark = SparkSession.builder.appName("test").getOrCreate()

data = [
    ("2018-01-01T11:00:00Z", "u1"),
    ("2018-01-01T12:00:00Z", "u1"),
    ("2018-01-01T11:00:00Z", "u2"),
    ("2018-01-02T11:00:00Z", "u2"),
    ("2018-03-01T12:15:00Z", "u1"),
    ("2018-03-01T14:00:00Z", "u1"),
    ("2018-01-01T15:30:00Z", "u1"),
    ("2018-01-01T16:20:00Z", "u1"),
    ("2018-01-01T16:50:00Z", "u1"),
    ("2018-01-01T11:00:00Z", "u2"),
    ("2018-01-02T11:00:00Z", "u2"),
    ("2018-01-01T18:20:00Z", "u1"),
    ("2018-01-01T16:50:00Z", "u3"),
    ("2018-01-01T11:00:00Z", "u3"),
    ("2018-01-02T11:00:00Z", "u3")
]
user_schema = StructType(
    [
    StructField('timestamp_col',StringType(),True),
    StructField('userid', StringType(), True)
])
user_df = spark.createDataFrame(data, user_schema)

user_df.show()
