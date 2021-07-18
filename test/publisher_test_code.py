#! /bin/python

import paho.mqtt.client as mqttclient
import time

connected = False

def on_connect(client,usedata,flags,rc):
    if rc == 0:
        print("client is connected")
        connected = True
    else:
        print("cannot connect to brocker")
        connected = False

connected = False
brocker_address="172.30.1.10"
port = 1884
user = "dodo"
password = "zepplim0"

client = mqttclient.Client("zigbee2mqtt")
client.username_pw_set(user,password=password)
client.on_connect = on_connect
client.connect(brocker_address,port=port)
client.loop_start()

while connected == False:
    time.sleep(0.2)
    client.publish("mqtt/firstcode","hello mqtt")
print("publish")
client.loop_stop()