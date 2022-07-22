from kafka import KafkaProducer
import json 

def build_json_producer(kafka_ips: list) -> KafkaProducer:

    return KafkaProducer(    
        bootstrap_servers=kafka_ips,
        value_serializer=lambda value: json.dumps(value).encode('utf-8')    
    )
