from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from datetime import datetime
import random
import uuid
import os
import json
from config import TOPIC

# Konfigurasi Schema Registry
schema_registry_conf = {
    'url': 'http://localhost:8081'
}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

# Path ke file skema Avro
schema_file_path = '/Users/wartadi/Desktop/alta/streaming-platform/pubsub/json/schemas/stock.avsc'

# Cek apakah file skema ada
if not os.path.exists(schema_file_path):
    raise FileNotFoundError(f"File tidak ditemukan: {schema_file_path}")

# Baca skema Avro dari file
with open(schema_file_path, 'r') as f:
    schema_str = f.read()

# Serializer Avro
avro_serializer = AvroSerializer(schema_registry_client, schema_str)

# Serializer untuk kunci
string_serializer = StringSerializer('utf_8')


def produce():
    producer = Producer({
        'bootstrap.servers': '34.101.224.54:19092',
        'client.id': 'python-producer'
    })

    def delivery_report(err, msg):
        if err is not None:
            print(f'Pengiriman pesan gagal: {err}')
        else:
            if msg is not None:
                print(f'Pesan terkirim ke {msg.topic()} [{msg.partition()}]')
            else:
                print('Pesan terkirim, tetapi tidak ada informasi yang tersedia.')

    try:
        while True:
            stock = {
                'event_time': datetime.now().isoformat(),
                'ticker': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
                'price': round(random.random() * 100, 2)
            }
            key = str(uuid.uuid4())
            try:
                # Serialize the value
                serialized_value = avro_serializer(stock, None)
                if serialized_value is None:
                    print("Gagal menyerialisasi nilai Avro.")
                    continue

                print(f"Mengirim pesan: {stock}")  # Debugging: Print the stock data being sent

                producer.produce(
                    topic=TOPIC,
                    key=string_serializer(key, None),
                    value=serialized_value,
                    callback=delivery_report
                )
                producer.produce(TOPIC, key=str(uuid.uuid4), value=json.dumps(stock), callback=delivery_report)  # Ensure proper polling to handle delivery reports
            except Exception as e:
                print(f"Error saat memproduksi pesan: {e}")
    except KeyboardInterrupt:
        print("Produksi dihentikan oleh pengguna.")

    # Tunggu untuk semua pesan yang belum dikirim
    producer.flush()

def main():
    produce()

if __name__ == "__main__":
    main()
