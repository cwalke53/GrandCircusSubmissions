from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import StructType, StructField, StringType, BooleanType, IntegerType

BOOTSTRAP_SERVERS = "confluent-local-broker-1:49808"
TOPIC = "wikimedia_events"

def main():
    spark = SparkSession.builder \
                        .appName('WikimediaLabInfo') \
                        .getOrCreate()

    # Read from the Kafka data stream
    kafkastream_df = spark.readStream.format("kafka") \
                                     .option('kafka.bootstrap.servers', BOOTSTRAP_SERVERS) \
                                     .option('subscribe', TOPIC) \
                                     .load()

    # Define a schema for JSON data
    schema = StructType([
        StructField("timestamp", IntegerType()),
        StructField("bot", BooleanType()),
        StructField("minor", BooleanType()),
        StructField("user", StringType()),
        StructField('meta', StructType([
            StructField('domain', StringType())
        ])),
        StructField("length", StructType([
            StructField("old", IntegerType()),
            StructField("new", IntegerType())
        ]))
    ])

    # Process and transform data
    stream_df = kafkastream_df.select(
        F.from_json(F.col('value').cast('string'), schema).alias('data')
    ).select(
        'data.timestamp', 'data.bot', 'data.minor', 'data.user', 
        F.col('data.meta.domain').alias('domain'),
        F.col('data.length.old').alias('old_length'),
        F.col('data.length.new').alias('new_length')
    ).withColumn(
        'length_diff', F.col('new_length') - F.col('old_length')
    )

    ### 1. Top Five Domains
    # top_five_domains = stream_df.groupBy('domain') \
    #                             .count() \
    #                             .orderBy(F.desc('count')) \
    #                             .limit(5)
    # query = top_five_domains.writeStream \
    #                          .outputMode('complete') \
    #                          .format('console') \
    #                          .start()

    ### 2. Top Five Users by Length Added
    # top_five_users = stream_df.groupBy('user') \
    #                           .agg(F.sum('length_diff').alias('total_length_diff')) \
    #                           .orderBy(F.desc('total_length_diff')) \
    #                           .limit(5)
    # query = top_five_users.writeStream \
    #                       .outputMode('complete') \
    #                       .format('console') \
    #                       .start()

    ### 3. Event Statistics
    event_stats = stream_df.agg(
        F.count('*').alias('total_events'),
        (F.sum(F.col('bot').cast('int')) / F.count('*')).alias('percent_bot'),
        F.avg('length_diff').alias('average_length_diff'),
        F.min('length_diff').alias('min_length_diff'),
        F.max('length_diff').alias('max_length_diff')
    )
    query = event_stats.writeStream \
                       .outputMode('complete') \
                       .format('console') \
                       .start()
    
    top_5_domains.writeStream.outputMode('complete').format('console').start()

    top_five_users.writeStream.outputMode('complete').format('console').start()
    
    event_stats.writeStream.outputMode('complete').format('console').start()







    
    stream_df.writeStream \
    .outputMode('append') \
    .option('checkpointLocation', 'output') \
    .option('path', 'output/latest_events.csv') \
    .option('header', True) \
    .trigger(processingTime='5 seconds') \
    .start()

    spark.streams.awaitAnyTermination()


if __name__ == "__main__":
    main()

