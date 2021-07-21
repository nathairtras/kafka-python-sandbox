#!/usr/bin/env bash
# Start the Docker containers for Zookeeper and Kafka
docker-compose up -d;

# Give Kafka a chance to spin up
echo "Pausing for Kafka to settle"
sleep 10;

# Create the sample topic
docker-compose exec kafka kafka-topics \
  --create \
  --zookeeper zookeeper:2181 \
  --replication-factor 1 \
  --partitions 2 \
  --topic default