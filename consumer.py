#!/usr/bin/env python3
import argparse
import json
from kafka import KafkaConsumer
from uuid import uuid4


# Set up consumer arguments with optional CLI overrides
parser = argparse.ArgumentParser(description='Set up a Kafka consumer')
parser.add_argument("--bootstrap-server", action="append")
parser.add_argument("--topic", action="append")
parser.add_argument("--group_id", default="default")
parser.add_argument("--client_id", default=str(uuid4()))
parser.add_argument("--auto_offset_reset", default="earliest")
parser.add_argument("--disable-auto-commit", action="store_false")
args = parser.parse_args()
print(args)

topics = args.topic or ["default"]
bootstrap_servers = args.bootstrap_server or ["localhost:9092"]

def key_deserializer(x):
    return x.decode('utf-8')

def value_deserializer(x):
    return json.loads(x.decode('utf-8'))


# Create a Kafka consumer
consumer = KafkaConsumer(
    *topics,
    bootstrap_servers=bootstrap_servers,
    group_id=args.group_id,
    client_id=args.client_id,
    auto_offset_reset=args.auto_offset_reset,
    enable_auto_commit=args.disable_auto_commit,
    key_deserializer=key_deserializer,
    value_deserializer=value_deserializer
)

# Print each message to console
for message in consumer:
    print(message)
