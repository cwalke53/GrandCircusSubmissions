from confluent_kafka import Consumer

# Kafka configuration
KAFKA_BOOTSTRAP_SERVERS = "localhost:55504"
KAFKA_TOPIC = "jokes"
GROUP_ID = "logger_group"

def main():
    # Configure the Kafka consumer
    consumer = Consumer({
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'group.id': GROUP_ID,
        'auto.offset.reset': 'earliest'
    })

    # Subscribe to topic
    consumer.subscribe([KAFKA_TOPIC])
    
    print("Joke Logger Consumer started...")
    try:
        while True:
            msg = consumer.poll(1.0)  # Poll for messages
            
            if msg is None:
                continue
            
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue
            
            # Extract and print the joke
            joke = msg.value().decode('utf-8')
            print(f"Joke: {joke}")
    except KeyboardInterrupt:
        print("Shutting down consumer...")
    finally:
        consumer.close()

if __name__ == "__main__":
    main()
