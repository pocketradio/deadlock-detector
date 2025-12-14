from confluent_kafka import Consumer
from ..config import BOOTSTRAP_SERVERS

consumer = Consumer({
    'bootstrap.servers' : BOOTSTRAP_SERVERS,
    'group.id' : 'test-group',
    'auto.offset.reset' : 'earliest'
})

consumer.subscribe(['graph-updates', 'deadlock-alerts'])


while True:
    msg = consumer.poll(0.5)
    if msg is None:
        continue

    if msg.error():
        print("Error",msg.error())
    else:
        print(f"Received : , key : {msg.key()} , value : {msg.value().decode()}") # decode to get json