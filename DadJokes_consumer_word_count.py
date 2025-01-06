from confluent_kafka import Consumer

# Kafka configuration
KAFKA_BOOTSTRAP_SERVERS = "localhost:55504"
KAFKA_TOPIC = "jokes"
GROUP_ID = "word_count_group"

def main():
    # Configure the Kafka consumer
    consumer = Consumer({
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'group.id': GROUP_ID,
        'auto.offset.reset': 'earliest'
    })

    # Subscribe to the topic
    consumer.subscribe([KAFKA_TOPIC])
    
    print("Word Count Consumer started...")
    
    joke_count = 0
    total_words = 0

    try:
        while True:
            msg = consumer.poll(1.0)  # Poll for messages
            
            if msg is None:
                continue
            
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue
            
            # Process the joke
            joke = msg.value().decode('utf-8')
            word_count = len(joke.split())
            joke_count += 1
            total_words += word_count
            
            print(f"Joke: {joke}")
            print(f"Word Count: {word_count}")
            
            # Batch processing: Calculate and log average every 5 jokes
            if joke_count % 5 == 0:
                average_word_count = total_words / joke_count
                print(f"--- Batch Processing ---")
                print(f"Jokes Received: {joke_count}")
                print(f"Cumulative Words: {total_words}")
                print(f"Average Word Count (last 5 jokes): {average_word_count:.2f}")
                print(f"------------------------")
    except KeyboardInterrupt:
        print("Shutting down consumer...")
    finally:
        consumer.close()

if __name__ == "__main__":
    main()
