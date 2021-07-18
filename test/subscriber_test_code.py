#! /bin/python

import paho.mqtt.client as mqttclient
import time

connected = False
message_received = False
button_status = [0,0,0,0]

def on_connect(client,usedata,flags,rc):
    if rc == 0:
        print("client is connected")
        connected = True
    else:
        print("cannot connect to brocker")
        connected = False

def on_message(client,userdata,message):
    # print("Message received" + str(message.payload.decode("utf-8")))
    msg = eval(message.payload.decode("utf-8"))
    # print(type(msg))
    if msg['state_l1'] == "ON" and button_status[0] == 0: 
        print("s1 is turn on")
        button_status[0] = 1
    elif msg['state_l1'] == "OFF": button_status[0] = 0

    if msg['state_l2'] == "ON" and button_status[1] == 0: 
        print("s2 is turn on")
        button_status[1] = 1
    elif msg['state_l2'] == "OFF": button_status[1] = 0

    if msg['state_l3'] == "ON" and button_status[2] == 0: 
        print("s3 is turn on")
        button_status[2] = 1
    elif msg['state_l3'] == "OFF": button_status[2] = 0

    if msg['state_l4'] == "ON" and button_status[3] == 0: 
        print("s4 is turn on")
        button_status[3] = 1
    elif msg['state_l4'] == "OFF": button_status[3] = 0

brocker_address="172.30.1.10"
port = 1884

client = mqttclient.Client("zigbee2mqtt")
client.on_message = on_message
client.on_connect = on_connect
client.connect(brocker_address,port=port)
client.loop_start()
client.subscribe("zigbee2mqtt/0x00124b0022ed0b1f")
while connected != True:
    time.sleep(0.2)
while message_received != True:
    time.sleep(0.2)
client.loop_stop()