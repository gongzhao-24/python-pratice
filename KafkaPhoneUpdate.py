from kafka import KafkaConsumer

consumer = KafkaConsumer('user_device_info_broadcast', bootstrap_servers=['124.251.115.187:9092'])
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(str(recv))
