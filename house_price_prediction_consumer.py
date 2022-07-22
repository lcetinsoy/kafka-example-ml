import json 
from kafka import KafkaConsumer
from model_utils import load_model, predict
from kafka_utils import build_json_producer
from db_utils import insert_predicted_price
topic_name = "house_price_prediction" 
 
consumer = KafkaConsumer(
    topic_name, 
    bootstrap_servers=["51.38.185.58"],
    value_deserializer= lambda byte_data: json.loads(byte_data.decode('utf-8')) 
)

for message in consumer: 
    print(message.value)
    for predicted_price in message.value['house_prices']:
        insert_predicted_price(predicted_price)