# kafka-python-sandbox
Docker-based sandbox for playing with Kafka and kafka-python.

* Uses Confluent images for creating Docker containers
* Provides example for multiple producers
* Demonstrates parallel consumers within a group

Try running things.
Change things.
Break things.
Fix things.
Learn things.

## Getting Started
### Prerequisites
* Create a virtual environment with [kafka-python](https://kafka-python.readthedocs.io/en/master/usage.html)
* Ensure Docker is installed and available

### Starting Kafka
Run `start-kafka.sh` to spin up Zookeeper and Kafka.
This will also create a `default` topic with two partitions.

### Producing and Consuming Messages
#### Starting a Consumer
A sample consumer is provided in `consumer.py`.
It will print the messages.
Configuration can be passed via command line arguments.

#### Starting a Producer
Now that a consumer is listening, we need to produce data.
A sample producer is provided in `producer.py`.
It generates 1000 messages each (of incrementing integers) for two keys.
Kafka will ensure all messages for a given key are in the same partition.
In this case, each key should be in a different partition.

Start the producer in a second terminal with the consumer running and you should see records printed by the consumer.

### Working with multiple consumers
If you have two consumers running before you start the producer, each consumer should grab one user's (one key's) data.
If instead you start one consumer, wait for messages to be received, then start another consumer, you will initially see one consumer reading from both partitions.

Manually handling partition assignment is outside the scope of this readme.

#### Working with multiple consumer groups
As configured, the consumer script has a default group set.
This means that all consumers should share the work of consuming the data.
If you want two consumers to each receive all messages, you need each consumer in a separate group.
This can be configured with a CLI flag.

## Cleanup
Run `stop-kafka.sh` to terminate the docker containers.
(This is just a friendly way to run `docker-compose down`.)

## References
* https://towardsdatascience.com/kafka-docker-python-408baf0e1088
* https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1
* https://kafka-python.readthedocs.io/en/master/usage.html
* https://kafka.apache.org/documentation/
* https://www.confluent.io/blog/5-things-every-kafka-developer-should-know/#tip-5-power-of-record-headers