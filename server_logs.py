from pyspark.sql import SparkSession, Window
import pyspark.sql.functions as F
from pyspark.sql.types import TimestampType, StringType, IntegerType

BOOTSTRAP_SERVERS = "confluent-local-broker-1:62215"
TOPIC = "server_logs"

# DATABASE SETTINGS
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USERNAME = "postgres"
DB_PASSWORD = "postgresql"
DB_URL = f"jdbc:postgresql://host.docker.internal:{DB_PORT}/{DB_NAME}"
DB_PROPERTIES = {"user": DB_USERNAME, "password": DB_PASSWORD, "driver": "org.postgresql.Driver"}

# Function to write logs to PostgreSQL
def write_logs_to_postgres(df, epoch_id):
    mode='append'
    table_name = 'server_logs'
    df.write.jdbc(url=DB_URL, table=table_name, mode=mode, properties=DB_PROPERTIES)

# Function to write errors to PostgreSQL
def write_errors_to_postgres(df, epoch_id):
    table_name='server_logs'
    mode='overwrite'
    df.write.jdbc(url=DB_URL, table=table_name, mode=mode, properties=DB_PROPERTIES)

def main():
    # Initialize SparkSession
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("Server_Logs_Processing") \
        .getOrCreate()
    

    # Read from Kafka
    kafka_stream_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", BOOTSTRAP_SERVERS) \
        .option("subscribe", TOPIC) \
        .load()

    # Process incoming Kafka data
    df = kafka_stream_df \
        .selectExpr("CAST(value AS STRING) as value") \
        .select(F.regexp_replace(F.col("value"), r'[\[\]"]', "").alias("cleaned_value")) \
        .select(F.split(F.col("cleaned_value"), " ").alias("data")) \
        .select(
            F.col("data").getItem(0).cast(StringType()).alias("ip_address"),
            F.col("data").getItem(1).cast(StringType()).alias("user_name"),
            F.col("data").getItem(2).cast(IntegerType()).alias("user_id"),
            F.col("data").getItem(3).cast(TimestampType()).alias("timestamp"),
            F.col("data").getItem(4).cast(StringType()).alias("http_method"),
            F.col("data").getItem(5).cast(StringType()).alias("path"),
            F.col("data").getItem(6).cast(IntegerType()).alias("status_code"),
        )

    df.writeStream.outputMode('append').format('console').start()
    # #Write logs to PostgreSQL
    df.writeStream \
        .outputMode("append") \
        .foreachBatch(write_logs_to_postgres) \
        .start()

    # #Top errors
    # filtered_df = df. filter((F.col("status_code") == 404) | (F.col("status_code") == 500))

# # Group by action_detail and count occurrences
#     df_agg =
# filtered_df.groupBy("path").agg(F.count_if(F.col"status_code")==404)-alias ("404_errors"),F.count_if(F.col("status_code")==500) -alias("'500_errors"), F.count(F.col("*")).alias("total").orderBy(F.col("total").desc())

#     df_agg.writeStream \
#     .outputMode("complete") \
#     .foreachBatch(write_errors_to_postgres2) \
#     .start()

#     # find aug click rate per user------
#     # window = Window. orderBy("ip_address")
#     window _duration = "1 minute"
# # Create a 1-minute tumbling window on the 'timestamp' column
#     window_spec = F.window("timestamp", "1 minute")

#     # Group by ip_address and window of 1 minute, and count the Logs
#     window_agg = df.withWatermark('timestamp', window_duration).groupBy(window_spec, "ip_address").count)

# # Include window time and window end
#     windowed_df = window_agg. select(
#     window_agg.window.start.alias("window_start"), window_agg.window.end.alias("window_end"),
#     "ip_address",
#     "count"
#     ) 

# # sort and add dos_attack column (boolean)
    # windowed_df = windowed_df.withColumn ("dos_attack", F.expr("count > 100")) \
    # .filter(F.col("dos_attack") == True) \
    # .orderBy(F.desc("count" ))
        
    # # Write DOS detection to console
    # windowed_df.writeStream \
    #     .outputMode("complete") \
    #     .format("console") \
    #     .start()

# this bit doesn't work:
    # fiLtered_df = windowed_df.filter(col("dos_ottack"）== True）

    # filtered_df.writestream.foreachBatchwrite_to_postgres).outputMode( 'append').start()




    
    spark.streams.awaitAnyTermination()

if __name__ == "__main__":
    main()
