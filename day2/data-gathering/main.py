import paho.mqtt.client as mqtt
import random
import time
client=mqtt.Client()
client.connect('broker.hivemq.com',1883)
print('Broker Connected')

while True:
    hum=random.randint(40,100)
    temp=random.randint(20,40)
    data={}
    data['hum']=hum
    data['temp']=temp
    client.publish('rcew/ml',str(data))
    print(data)
    time.sleep(2)