from confluent_kafka import Consumer, KafkaException
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka.serialization import SerializationContext, MessageField
from config import TOPIC

# Konfigurasi Schema Registry
schema_registry_conf = {
    'url': 'http://localhost:8081'
}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

# Skema Avro sebagai string
schema_str = """
{
  "namespace": "example.avro",
  "type": "record",
  "name": "Stock",
  "fields": [
    {"name": "event_time", "type": "string"},
    {"name": "ticker", "type": "string"},
    {"name": "price", "type": "float"}
  ]
}
"""

# Deserializer Avro
avro_deserializer = AvroDeserializer(schema_registry_client, schema_str)

def create_consumer():
    consumer_conf = {
        'bootstrap.servers': '34.101.224.54:19092',
        'group.id': 'my_consumer_group',  # Ganti dengan ID grup konsumer Anda
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': True,
    }
    return Consumer(consumer_conf)

def consume():
    consumer = create_consumer()
    consumer.subscribe([TOPIC])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition
                    continue
                else:
                    raise KafkaException(msg.error())

            # Deserialisasi menggunakan AvroDeserializer
            value = avro_deserializer(msg.value(), SerializationContext(TOPIC, MessageField.VALUE))
            print(f"Pesan diterima: {value}")

    except KeyboardInterrupt:
        print("Konsumer dihentikan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        consumer.close()

def main():
    consume()

if __name__ == "__main__":
    main()
