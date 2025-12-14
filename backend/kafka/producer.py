from confluent_kafka import Producer
import json
import uuid

producer = Producer({
    'bootstrap.servers' : 'localhost:9092'
})

sim_id = str(uuid.uuid4()) # for partitioning

def produce(topic, data : object):

    json_string = json.dumps(data, indent=2)
    producer.produce(
        topic,
        key = sim_id,
        value = json_string
    )
    producer.flush()