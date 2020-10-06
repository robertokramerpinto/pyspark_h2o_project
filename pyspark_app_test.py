from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('test').getOrCreate()

if __name__ == '__main__':
    print(spark)