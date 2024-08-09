from confluent_kafka import KafkaError, KafkaException
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError

def consume():
    config = {
        'bootstrap.servers': '34.101.224.54:19092',
        'group.id': 'clickstream-wartadi-group',  # Nama grup consumer
        'schema.registry.url': 'http://34.101.224.54:18081',
        'auto.offset.reset': 'earliest'  # Memulai dari awal jika tidak ada offset yang disimpan
    }

    consumer = AvroConsumer(config)
    consumer.subscribe(['clickstream_wartadi'])

    try:
        while True:
            try:
                message = consumer.poll(1.0)  # Tunggu 1 detik untuk pesan

                if message is None:
                    continue

                if message.error():
                    if message.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        print(f"Reached end at {message.topic()} [{message.partition()}] offset {message.offset()}")
                    else:
                        raise KafkaException(message.error())
                else:
                    # Pesan diterima dan didecode
                    print(f"Consumed message from topic {message.topic()}, partition {message.partition()}, offset {message.offset()}")
                    print(f"Key: {message.key()}, Value: {message.value()}")

            except SerializerError as e:
                # Kesalahan dalam deserialization
                print(f"Message deserialization failed: {e}")
                continue

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        print("Consumer closed")

def main():
    consume()

if __name__ == "__main__":
    main()
