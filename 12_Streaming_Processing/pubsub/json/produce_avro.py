from confluent_kafka import avro
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka import Producer
from confluent_kafka.serialization import SerializationContext, MessageField
from datetime import datetime
import random
import uuid
from config import TOPIC

# Definisikan schema Avro
schema_file_path = '/Users/wartadi/Desktop/alta/streaming-platform/pubsub/json/schemas/stock.avsc'

def load_schema(schema_file_path):
    with open(schema_file_path, 'r') as file:
        schema_str = file.read()
    return schema_str  # Kembalikan schema sebagai string

schema_str = load_schema(schema_file_path)

# Buat Serializer untuk value
def create_avro_serializer(schema_registry_url, schema_str):
    schema_registry_client = SchemaRegistryClient({'url': schema_registry_url})
    return AvroSerializer(schema_registry_client, schema_str)  # Gunakan schema_str sebagai string

def create_producer():
    return Producer({
        'bootstrap.servers': '34.101.224.54:19092',
    })

def produce():
    # Buat Producer
    p = create_producer()

    # Buat AvroSerializer
    avro_serializer = create_avro_serializer('http://34.101.224.54:8085', schema_str)  # Ganti dengan URL Schema Registry Anda

    def delivery_report(err, msg):
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    try:
        while True:
            stock = {
                'event_time': datetime.now().isoformat(),
                'ticker': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
                'price': round(random.random() * 100, 2)
            }
            # Serialisasi menggunakan AvroSerializer
            value = avro_serializer(stock, SerializationContext(TOPIC, MessageField.VALUE))
            p.produce(topic=TOPIC, key=str(uuid.uuid4()), value=value, on_delivery=delivery_report)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        p.flush()

def main():
    produce()

if __name__ == "__main__":
    main()
