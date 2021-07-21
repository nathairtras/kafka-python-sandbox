#!/usr/bin/env python3
import argparse
import json
import time
from kafka import KafkaProducer
from uuid import uuid4


# Set up producer arguments with optional CLI overrides
parser = argparse.ArgumentParser(description='Set up a Kafka producer')
parser.add_argument("--bootstrap-server", action="append")
parser.add_argument("--topic", default="default")
parser.add_argument("--client-id", default=str(uuid4()))
args = parser.parse_args()


bootstrap_servers = args.bootstrap_server or ["localhost:9092"]


def key_serializer(x):
    return x.encode('utf-8')


def value_serializer(x):
    return json.dumps(x).encode('utf-8')


# Start a producer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    key_serializer=key_serializer,
    value_serializer=value_serializer,
)

headers = [
  ("client_id", args.client_id.encode('utf-8'))
]

# Write some data
for e in range(1000):
    for k in ['user_1', 'user_2']:
        producer.send(args.topic, key=k, value=e, headers=headers)
    time.sleep(5)
