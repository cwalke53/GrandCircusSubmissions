import time
import requests
from confluent_kafka import Producer

# Kafka configuration
KAFKA_BOOTSTRAP_SERVERS = "localhost:55504"  
KAFKA_TOPIC = "jokes"

# Callback to confirm message delivery
def delivery_callback(err, msg):
    if err:
        print(f"Message failed delivery: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [partition: {msg.partition()}]")

def main():
    # Configure the Kafka producer
    producer = Producer({'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS})
    
    while True:
        # Fetch a joke from the API
        response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        if response.status_code == 200:
            joke_data = response.json()
            joke = joke_data.get("joke")
            
            # Publish the joke to Kafka
            producer.produce(KAFKA_TOPIC, value=joke, callback=delivery_callback)
            producer.flush()
            print(f"Published joke: {joke}")
        else:
            print("Failed to fetch joke from API.")
        
        time.sleep(5)  # Fetch a new joke every 5 seconds

if __name__ == "__main__":
    main()
