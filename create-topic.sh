# Create the sample topic
docker-compose exec kafka kafka-topics \
  --create \
  --zookeeper zookeeper:2181 \
  --replication-factor 1 \
  --partitions 2 \
  --topic $1