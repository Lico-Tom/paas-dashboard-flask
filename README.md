# paas-dashboard-flask

## Test environment

```
PD_KAFKA_DEFAULT_BOOTSTRAP_SERVERS=localhost:9092
PD_MONGO_DEFAULT_HOST=localhost
PD_MONGO_DEFAULT_PORT=27017
PD_PULSAR_DEFAULT_HOST=localhost
PD_PULSAR_DEFAULT_TCP_PORT=6650
PD_PULSAR_DEFAULT_WEB_PORT=8080
PD_REDIS_DEFAULT_URL=redis://localhost:6379
PD_REDIS_DEFAULT_CLUSTER_URL=redis://localhost:6379
PD_ROCKETMQ_DEFAULT_NAMESRV_ADDR=localhost:9876
PD_ROCKETMQ_DEFAULT_CLUSTER=DefaultCluster
PD_ZOOKEEPER_DEFAULT_ADDR=zookeeper-0.svc-zookeeper:2181
```

## generate requirements.txt
```bash
pip install pipreqs
pipreqs --encoding utf-8 . --force
```
